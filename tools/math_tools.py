# Math utility functions
import math
import statistics

# Basic arithmetic operations
def add(*args):
    """Add multiple numbers."""
    if not args:
        return 0
    return sum(args)

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(*args):
    """Multiply multiple numbers."""
    if not args:
        return 0
    result = 1
    for num in args:
        result *= num
    return result

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulo(a, b):
    """Calculate a modulo b (remainder)."""
    if b == 0:
        raise ValueError("Cannot calculate modulo by zero")
    return a % b

def floor_divide(a, b):
    """Floor division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

# Power and root operations
def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def square(n):
    """Calculate square of n."""
    return n ** 2

def cube(n):
    """Calculate cube of n."""
    return n ** 3

def square_root(n):
    """Calculate square root of n."""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(n)

def cube_root(n):
    """Calculate cube root of n."""
    if n < 0:
        return -(abs(n) ** (1/3))
    return n ** (1/3)

def nth_root(n, root):
    """Calculate nth root of n."""
    if root == 0:
        raise ValueError("Cannot calculate 0th root")
    if n < 0 and root % 2 == 0:
        raise ValueError("Cannot calculate even root of negative number")
    if n < 0:
        return -(abs(n) ** (1/root))
    return n ** (1/root)

# Statistical operations
def average(*args):
    """Calculate average (mean) of multiple numbers."""
    if not args:
        raise ValueError("Cannot calculate average of empty list")
    return sum(args) / len(args)

def mean(*args):
    """Calculate arithmetic mean of multiple numbers."""
    if not args:
        raise ValueError("Cannot calculate mean of empty list")
    return statistics.mean(args)

def median(*args):
    """Calculate median of multiple numbers."""
    if not args:
        raise ValueError("Cannot calculate median of empty list")
    return statistics.median(args)

def mode(*args):
    """Calculate mode of multiple numbers."""
    if not args:
        raise ValueError("Cannot calculate mode of empty list")
    try:
        return statistics.mode(args)
    except statistics.StatisticsError:
        return "No unique mode found"

def range_values(*args):
    """Calculate range (max - min) of multiple numbers."""
    if not args:
        raise ValueError("Cannot calculate range of empty list")
    return max(args) - min(args)

def variance(*args):
    """Calculate variance of multiple numbers."""
    if len(args) < 2:
        raise ValueError("Need at least 2 values to calculate variance")
    return statistics.variance(args)

def standard_deviation(*args):
    """Calculate standard deviation of multiple numbers."""
    if len(args) < 2:
        raise ValueError("Need at least 2 values to calculate standard deviation")
    return statistics.stdev(args)

# Advanced math functions
def absolute(n):
    """Calculate absolute value of n."""
    return abs(n)

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if not isinstance(n, int):
        raise ValueError("Factorial is only defined for integers")
    return math.factorial(n)

def gcd(*args):
    """Calculate greatest common divisor of multiple numbers."""
    if not args:
        raise ValueError("Cannot calculate GCD of empty list")
    result = args[0]
    for num in args[1:]:
        result = math.gcd(result, num)
    return result

def lcm(*args):
    """Calculate least common multiple of multiple numbers."""
    if not args:
        raise ValueError("Cannot calculate LCM of empty list")
    result = args[0]
    for num in args[1:]:
        result = abs(result * num) // math.gcd(result, num)
    return result

def percentage(value, total):
    """Calculate percentage of value in total."""
    if total == 0:
        raise ValueError("Cannot calculate percentage with zero total")
    return (value / total) * 100

def percentage_change(old_value, new_value):
    """Calculate percentage change from old to new value."""
    if old_value == 0:
        raise ValueError("Cannot calculate percentage change from zero")
    return ((new_value - old_value) / old_value) * 100

# Trigonometric functions
def sin(angle_degrees):
    """Calculate sine of angle in degrees."""
    return math.sin(math.radians(angle_degrees))

def cos(angle_degrees):
    """Calculate cosine of angle in degrees."""
    return math.cos(math.radians(angle_degrees))

def tan(angle_degrees):
    """Calculate tangent of angle in degrees."""
    return math.tan(math.radians(angle_degrees))

def asin(value):
    """Calculate arcsine in degrees."""
    if value < -1 or value > 1:
        raise ValueError("Value must be between -1 and 1")
    return math.degrees(math.asin(value))

def acos(value):
    """Calculate arccosine in degrees."""
    if value < -1 or value > 1:
        raise ValueError("Value must be between -1 and 1")
    return math.degrees(math.acos(value))

def atan(value):
    """Calculate arctangent in degrees."""
    return math.degrees(math.atan(value))

# Logarithmic functions
def log(n, base=math.e):
    """Calculate logarithm of n with given base (default: natural log)."""
    if n <= 0:
        raise ValueError("Cannot calculate log of non-positive number")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(n, base)

def log10(n):
    """Calculate base-10 logarithm of n."""
    if n <= 0:
        raise ValueError("Cannot calculate log of non-positive number")
    return math.log10(n)

def log2(n):
    """Calculate base-2 logarithm of n."""
    if n <= 0:
        raise ValueError("Cannot calculate log of non-positive number")
    return math.log2(n)

def natural_log(n):
    """Calculate natural logarithm of n."""
    if n <= 0:
        raise ValueError("Cannot calculate log of non-positive number")
    return math.log(n)

# Exponential functions
def exp(n):
    """Calculate e raised to the power of n."""
    return math.exp(n)

def exp2(n):
    """Calculate 2 raised to the power of n."""
    return 2 ** n

def exp10(n):
    """Calculate 10 raised to the power of n."""
    return 10 ** n

# Rounding functions
def round_number(n, decimals=0):
    """Round number to specified decimal places."""
    return round(n, decimals)

def ceiling(n):
    """Round up to nearest integer."""
    return math.ceil(n)

def floor(n):
    """Round down to nearest integer."""
    return math.floor(n)

def truncate(n):
    """Remove decimal part (truncate towards zero)."""
    return math.trunc(n)

# Min/Max operations
def minimum(*args):
    """Find minimum value among multiple numbers."""
    if not args:
        raise ValueError("Cannot find minimum of empty list")
    return min(args)

def maximum(*args):
    """Find maximum value among multiple numbers."""
    if not args:
        raise ValueError("Cannot find maximum of empty list")
    return max(args)

# Comparison functions
def greater_than(a, b):
    """Check if a is greater than b."""
    return a > b

def less_than(a, b):
    """Check if a is less than b."""
    return a < b

def equal_to(a, b):
    """Check if a equals b."""
    return a == b

def greater_than_or_equal(a, b):
    """Check if a is greater than or equal to b."""
    return a >= b

def less_than_or_equal(a, b):
    """Check if a is less than or equal to b."""
    return a <= b

def not_equal_to(a, b):
    """Check if a is not equal to b."""
    return a != b

def compare(a, b, operator):
    """Compare two values using specified operator."""
    if operator == ">":
        return a > b
    elif operator == "<":
        return a < b
    elif operator == "==" or operator == "=":
        return a == b
    elif operator == ">=" or operator == "≥":
        return a >= b
    elif operator == "<=" or operator == "≤":
        return a <= b
    elif operator == "!=" or operator == "≠":
        return a != b
    else:
        raise ValueError(f"Unknown operator: {operator}")

# Number properties
def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if number is odd."""
    return n % 2 != 0

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_positive(n):
    """Check if number is positive."""
    return n > 0

def is_negative(n):
    """Check if number is negative."""
    return n < 0

def is_zero(n):
    """Check if number is zero."""
    return n == 0 