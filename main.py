#!/usr/bin/env python3
"""
Tool-Enhanced Reasoning Script
Processes natural language queries using LLM and executes appropriate tools.
"""

import os
import json
import importlib
import inspect
from typing import Dict, Any, List
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables  
import os as _os
env_path = _os.path.join(_os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

class ToolRegistry:
    """Registry for dynamically loading and managing tools."""
    
    def __init__(self):
        self.tools = {}
        self.load_tools()
    
    def load_tools(self):
        """Load all tools from the tools directory."""
        tool_modules = ['tools.math_tools', 'tools.string_tools']
        
        for module_name in tool_modules:
            try:
                module = importlib.import_module(module_name)
                tool_name = module_name.split('.')[-1]  # e.g., 'math_tools'
                
                # Get all functions from the module
                functions = {}
                for name, obj in inspect.getmembers(module):
                    if inspect.isfunction(obj) and not name.startswith('_'):
                        functions[name] = obj
                
                self.tools[tool_name] = functions
                print(f"✅ Loaded {len(functions)} functions from {tool_name}")
                
            except ImportError as e:
                print(f"❌ Failed to load {module_name}: {e}")
    
    def get_function(self, tool_name: str, function_name: str):
        """Get a specific function from a tool."""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        if function_name not in self.tools[tool_name]:
            raise ValueError(f"Function '{function_name}' not found in {tool_name}")
        
        return self.tools[tool_name][function_name]
    
    def get_tool_descriptions(self) -> str:
        """Generate tool descriptions for LLM prompt."""
        descriptions = []
        
        for tool_name, functions in self.tools.items():
            descriptions.append(f"\n## {tool_name.upper()}:")
            
            for func_name, func in functions.items():
                # Get function signature
                sig = inspect.signature(func)
                docstring = inspect.getdoc(func) or "No description available"
                
                descriptions.append(f"- {func_name}{sig}: {docstring}")
        
        return "\n".join(descriptions)

class StepExecutor:
    """Executes operations step by step with variable storage."""
    
    def __init__(self, tool_registry: ToolRegistry):
        self.tool_registry = tool_registry
        self.variables = {}
        self.execution_log = []
    
    def resolve_argument(self, arg):
        """Resolve argument - could be a value or a stored variable."""
        if isinstance(arg, str) and arg in self.variables:
            return self.variables[arg]
        return arg
    
    def execute_step(self, step: Dict[str, Any]) -> Any:
        """Execute a single step operation."""
        try:
            tool_name = step['tool']
            function_name = step['function']
            arguments = step.get('arguments', [])
            store_as = step.get('store_as')
            description = step.get('description', f"Execute {function_name}")
            
            # Resolve all arguments
            resolved_args = [self.resolve_argument(arg) for arg in arguments]
            
            # Get and call the function
            func = self.tool_registry.get_function(tool_name, function_name)
            result = func(*resolved_args)
            
            # Store result if needed
            if store_as:
                self.variables[store_as] = result
            
            # Log execution
            log_entry = {
                'step': step.get('step', len(self.execution_log) + 1),
                'description': description,
                'function': f"{tool_name}.{function_name}",
                'arguments': resolved_args,
                'result': result
            }
            self.execution_log.append(log_entry)
            
            print(f"Step {log_entry['step']}: {description}")
            print(f"  → {function_name}({', '.join(map(str, resolved_args))}) = {result}")
            
            return result
            
        except Exception as e:
            error_msg = f"Error in step {step.get('step', '?')}: {str(e)}"
            print(f"❌ {error_msg}")
            raise RuntimeError(error_msg)
    
    def execute_operations(self, operations: List[Dict[str, Any]]) -> Any:
        """Execute all operations in sequence."""
        final_result = None
        
        print(f"\n🔄 Executing {len(operations)} operation(s)...")
        print("-" * 50)
        
        for operation in operations:
            result = self.execute_step(operation)
            final_result = result
        
        return final_result

class LLMProcessor:
    """Handles communication with Gemini LLM."""
    
    def __init__(self, tool_registry: ToolRegistry):
        self.tool_registry = tool_registry
        
        # Configure Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def create_system_prompt(self) -> str:
        """Create system prompt with tool descriptions."""
        tool_descriptions = self.tool_registry.get_tool_descriptions()
        
        return f"""You are a tool-calling planner. Your job is to analyze user queries and create a JSON plan for executing operations using available tools.

AVAILABLE TOOLS:{tool_descriptions}

IMPORTANT RULES:
1. You MUST respond ONLY with valid JSON - no explanations, no text outside JSON
2. You MUST NOT calculate or provide answers - only create execution plans
3. Break complex operations into steps respecting order of operations
4. Use "store_as" to save intermediate results for later steps
5. Reference stored results by their variable name in later steps
6. ALWAYS use lowercase tool names: "math_tools" and "string_tools" (NOT "MATH_TOOLS")

JSON FORMAT:
{{
  "reasoning": "Brief explanation of your approach",
  "operations": [
    {{
      "step": 1,
      "tool": "tool_name",
      "function": "function_name",
      "arguments": [arg1, arg2, ...],
      "store_as": "variable_name",
      "description": "What this step does"
    }}
  ]
}}

EXAMPLES:
Query: "What's 2 + 3 * 4?"
Response:
{{
  "reasoning": "Multiply first (order of operations), then add",
  "operations": [
    {{
      "step": 1,
      "tool": "math_tools",
      "function": "multiply",
      "arguments": [3, 4],
      "store_as": "mult_result",
      "description": "Calculate 3 * 4"
    }},
    {{
      "step": 2,
      "tool": "math_tools",
      "function": "add",
      "arguments": [2, "mult_result"],
      "store_as": "final_result",
      "description": "Add 2 to the multiplication result"
    }}
  ]
}}"""
    
    def process_query(self, user_query: str) -> Dict[str, Any]:
        """Process user query and return execution plan."""
        system_prompt = self.create_system_prompt()
        
        full_prompt = f"{system_prompt}\n\nUser Query: {user_query}\n\nResponse:"
        
        try:
            response = self.model.generate_content(full_prompt)
            response_text = response.text.strip()
            
            # Save LLM response to file (will be cleared for each new prompt)
            self.save_llm_response_to_file(user_query, response_text)
            
            print(f"🤖 LLM Response saved to 'llm_response.txt'")
            print("-" * 50)
            
            # Parse JSON response (handle markdown formatting)
            try:
                # Remove markdown code blocks if present
                if response_text.startswith("```json"):
                    response_text = response_text.replace("```json", "").replace("```", "").strip()
                elif response_text.startswith("```"):
                    response_text = response_text.replace("```", "").strip()
                
                return json.loads(response_text)
            except json.JSONDecodeError as e:
                print(f"🔍 Debug - Raw response: {repr(response_text)}")
                raise ValueError(f"Invalid JSON response from LLM: {e}")
                
        except Exception as e:
            raise RuntimeError(f"Failed to get response from LLM: {e}")
    
    def save_llm_response_to_file(self, user_query: str, response_text: str):
        """Save LLM response and query details to file."""
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# Tool-Enhanced Reasoning System - Query Results
Generated: {timestamp}

## User Query:
{user_query}

## LLM Response (Raw JSON):
{response_text}

## Parsed Operations:
"""
        
        try:
            # Try to parse and format the JSON nicely
            if response_text.startswith("```json"):
                json_text = response_text.replace("```json", "").replace("```", "").strip()
            elif response_text.startswith("```"):
                json_text = response_text.replace("```", "").strip()
            else:
                json_text = response_text
            
            parsed_json = json.loads(json_text)
            content += json.dumps(parsed_json, indent=2)
        except:
            content += "Failed to parse JSON"
        
        # Write to file (overwrites previous content)
        with open("llm_response.txt", "w", encoding="utf-8") as f:
            f.write(content)

class ToolEnhancedReasoning:
    """Main orchestrator for the tool-enhanced reasoning system."""
    
    def __init__(self):
        print("🚀 Initializing Tool-Enhanced Reasoning System...")
        self.tool_registry = ToolRegistry()
        self.llm_processor = LLMProcessor(self.tool_registry)
        print("✅ System ready!")
    
    def process_query(self, user_query: str):
        """Process a user query end-to-end."""
        print(f"\n📝 Query: {user_query}")
        print("=" * 60)
        
        try:
            # Get execution plan from LLM
            plan = self.llm_processor.process_query(user_query)
            
            # Validate plan structure
            if 'operations' not in plan:
                raise ValueError("Invalid plan: missing 'operations' field")
            
            # Execute the plan
            executor = StepExecutor(self.tool_registry)
            final_result = executor.execute_operations(plan['operations'])
            
            # Save execution results to file
            self.save_execution_results_to_file(user_query, plan, executor, final_result)
            
            # Display results
            print("-" * 50)
            print(f"🎯 Final Result: {final_result}")
            print(f"📄 Complete results saved to 'llm_response.txt'")
            
            if len(executor.execution_log) > 1:
                print(f"\n📊 Execution Summary:")
                for log in executor.execution_log:
                    print(f"  Step {log['step']}: {log['description']} → {log['result']}")
            
            return final_result
            
        except Exception as e:
            error_msg = f"❌ Error: {e}"
            print(error_msg)
            # Save error to file as well
            self.save_error_to_file(user_query, str(e))
            return None
    
    def save_execution_results_to_file(self, user_query: str, plan: Dict[str, Any], executor: 'StepExecutor', final_result: Any):
        """Append execution results to the response file."""
        try:
            # Read existing content
            with open("llm_response.txt", "r", encoding="utf-8") as f:
                content = f.read()
            
            # Append execution details
            content += f"\n\n## Execution Results:\n"
            content += f"**Final Result:** {final_result}\n\n"
            
            if executor.execution_log:
                content += "### Step-by-Step Execution:\n"
                for log in executor.execution_log:
                    content += f"- **Step {log['step']}:** {log['description']}\n"
                    content += f"  - Function: `{log['function']}`\n"
                    content += f"  - Arguments: {log['arguments']}\n"
                    content += f"  - Result: `{log['result']}`\n\n"
            
            # Variables used
            if executor.variables:
                content += "### Variables Stored:\n"
                for var_name, var_value in executor.variables.items():
                    content += f"- **{var_name}:** {var_value}\n"
                content += "\n"
            
            # Write back to file
            with open("llm_response.txt", "w", encoding="utf-8") as f:
                f.write(content)
                
        except Exception as e:
            print(f"⚠️ Failed to save execution results to file: {e}")
    
    def save_error_to_file(self, user_query: str, error_message: str):
        """Save error information to file."""
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# Tool-Enhanced Reasoning System - Error Report
Generated: {timestamp}

## User Query:
{user_query}

## Error:
{error_message}

## Status:
Query execution failed. Please check your query and try again.
"""
        
        try:
            with open("llm_response.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"⚠️ Failed to save error to file: {e}")
    
    def interactive_mode(self):
        """Run in interactive mode."""
        print(f"\n🎮 Interactive Mode - Type 'quit' to exit")
        print("=" * 60)
        
        while True:
            try:
                query = input("\n💬 Enter your query: ").strip()
                
                if query.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not query:
                    print("Please enter a valid query.")
                    continue
                
                self.process_query(query)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")

def main():
    """Main entry point."""
    try:
        # Initialize the system
        reasoning_system = ToolEnhancedReasoning()
        
        # Enter interactive mode directly
        reasoning_system.interactive_mode()
        
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        print("Make sure you have:")
        print("1. Created a .env file with GEMINI_API_KEY")
        print("2. Installed dependencies: pip install -r requirements.txt")

if __name__ == "__main__":
    main() 