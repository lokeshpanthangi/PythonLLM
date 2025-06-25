# String utility functions
import re
import string

# Character counting functions
def count_vowels(text):
    """Count the number of vowels in text."""
    if not text:
        return 0
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    """Count the number of consonants in text."""
    if not text:
        return 0
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

def count_letters(text):
    """Count the number of letters in text."""
    if not text:
        return 0
    return sum(1 for char in text if char.isalpha())

def count_digits(text):
    """Count the number of digits in text."""
    if not text:
        return 0
    return sum(1 for char in text if char.isdigit())

def count_words(text):
    """Count the number of words in text."""
    if not text:
        return 0
    return len(text.split())

def count_sentences(text):
    """Count the number of sentences in text."""
    if not text:
        return 0
    sentence_endings = '.!?'
    return sum(1 for char in text if char in sentence_endings)

def count_paragraphs(text):
    """Count the number of paragraphs in text."""
    if not text:
        return 0
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    return len(paragraphs)

def count_characters(text):
    """Count total number of characters including spaces."""
    if not text:
        return 0
    return len(text)

def count_characters_no_spaces(text):
    """Count characters excluding spaces."""
    if not text:
        return 0
    return len(text.replace(" ", ""))

def count_specific_char(text, char):
    """Count occurrences of a specific character."""
    if not text:
        return 0
    return text.count(char)

def count_uppercase_letters(text):
    """Count uppercase letters in text."""
    if not text:
        return 0
    return sum(1 for char in text if char.isupper())

def count_lowercase_letters(text):
    """Count lowercase letters in text."""
    if not text:
        return 0
    return sum(1 for char in text if char.islower())

def count_punctuation(text):
    """Count punctuation marks in text."""
    if not text:
        return 0
    return sum(1 for char in text if char in string.punctuation)

def count_whitespace(text):
    """Count whitespace characters in text."""
    if not text:
        return 0
    return sum(1 for char in text if char.isspace())

# Case conversion functions
def uppercase(s):
    """Convert string to uppercase."""
    return s.upper()

def lowercase(s):
    """Convert string to lowercase."""
    return s.lower()

def capitalize_first(s):
    """Capitalize only the first character."""
    return s.capitalize()

def capitalize_words(s):
    """Capitalize the first letter of each word."""
    return s.title()

def swap_case(s):
    """Swap the case of all letters."""
    return s.swapcase()

def camel_case(s):
    """Convert to camelCase."""
    words = s.split()
    if not words:
        return s
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def pascal_case(s):
    """Convert to PascalCase."""
    words = s.split()
    return ''.join(word.capitalize() for word in words)

def snake_case(s):
    """Convert to snake_case."""
    # Replace spaces with underscores and convert to lowercase
    return re.sub(r'\s+', '_', s.strip()).lower()

def kebab_case(s):
    """Convert to kebab-case."""
    # Replace spaces with hyphens and convert to lowercase
    return re.sub(r'\s+', '-', s.strip()).lower()

# String manipulation functions
def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def reverse_words(s):
    """Reverse the order of words in a string."""
    return ' '.join(s.split()[::-1])

def remove_spaces(s):
    """Remove all spaces from string."""
    return s.replace(" ", "")

def remove_whitespace(s):
    """Remove all whitespace characters from string."""
    return re.sub(r'\s+', '', s)

def trim_whitespace(s):
    """Remove leading and trailing whitespace."""
    return s.strip()

def compress_whitespace(s):
    """Replace multiple whitespace characters with single space."""
    return re.sub(r'\s+', ' ', s.strip())

def remove_punctuation(s):
    """Remove all punctuation from string."""
    return s.translate(str.maketrans('', '', string.punctuation))

def remove_digits(s):
    """Remove all digits from string."""
    return ''.join(char for char in s if not char.isdigit())

def remove_letters(s):
    """Remove all letters from string."""
    return ''.join(char for char in s if not char.isalpha())

def keep_only_letters(s):
    """Keep only letters in string."""
    return ''.join(char for char in s if char.isalpha())

def keep_only_digits(s):
    """Keep only digits in string."""
    return ''.join(char for char in s if char.isdigit())

def keep_only_alphanumeric(s):
    """Keep only letters and digits."""
    return ''.join(char for char in s if char.isalnum())

# String analysis functions
def is_palindrome(s):
    """Check if string is a palindrome."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def is_anagram(s1, s2):
    """Check if two strings are anagrams."""
    clean_s1 = ''.join(char.lower() for char in s1 if char.isalpha())
    clean_s2 = ''.join(char.lower() for char in s2 if char.isalpha())
    return sorted(clean_s1) == sorted(clean_s2)

def is_all_uppercase(s):
    """Check if all letters in string are uppercase."""
    return s.isupper() and any(char.isalpha() for char in s)

def is_all_lowercase(s):
    """Check if all letters in string are lowercase."""
    return s.islower() and any(char.isalpha() for char in s)

def is_title_case(s):
    """Check if string is in title case."""
    return s.istitle()

def is_alphanumeric(s):
    """Check if string contains only letters and digits."""
    return s.isalnum() and len(s) > 0

def is_alphabetic(s):
    """Check if string contains only letters."""
    return s.isalpha() and len(s) > 0

def is_numeric(s):
    """Check if string contains only digits."""
    return s.isdigit() and len(s) > 0

def contains_substring(text, substring):
    """Check if text contains substring."""
    return substring in text

def starts_with(text, prefix):
    """Check if text starts with prefix."""
    return text.startswith(prefix)

def ends_with(text, suffix):
    """Check if text ends with suffix."""
    return text.endswith(suffix)

# String searching and replacing
def find_substring(text, substring):
    """Find first occurrence of substring (returns index or -1)."""
    return text.find(substring)

def find_all_substrings(text, substring):
    """Find all occurrences of substring (returns list of indices)."""
    indices = []
    start = 0
    while True:
        index = text.find(substring, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices

def replace_substring(text, old, new):
    """Replace all occurrences of old substring with new."""
    return text.replace(old, new)

def replace_first_occurrence(text, old, new):
    """Replace only the first occurrence of old substring with new."""
    return text.replace(old, new, 1)

def insert_at_position(text, position, insert_text):
    """Insert text at specified position."""
    if position < 0 or position > len(text):
        raise ValueError("Position out of range")
    return text[:position] + insert_text + text[position:]

def remove_substring(text, substring):
    """Remove all occurrences of substring."""
    return text.replace(substring, "")

# String extraction functions
def get_first_word(text):
    """Get the first word from text."""
    words = text.split()
    return words[0] if words else ""

def get_last_word(text):
    """Get the last word from text."""
    words = text.split()
    return words[-1] if words else ""

def get_word_at_position(text, position):
    """Get word at specified position (0-indexed)."""
    words = text.split()
    if 0 <= position < len(words):
        return words[position]
    else:
        raise ValueError("Position out of range")

def get_substring(text, start, end):
    """Get substring from start to end position."""
    if start < 0 or end > len(text) or start > end:
        raise ValueError("Invalid start or end position")
    return text[start:end]

def get_characters_at_positions(text, positions):
    """Get characters at specified positions."""
    result = ""
    for pos in positions:
        if 0 <= pos < len(text):
            result += text[pos]
    return result

# String formatting functions
def repeat_string(text, times):
    """Repeat string specified number of times."""
    if times < 0:
        raise ValueError("Times must be non-negative")
    return text * times

def center_string(text, width, fill_char=' '):
    """Center string within specified width."""
    return text.center(width, fill_char)

def left_justify(text, width, fill_char=' '):
    """Left justify string within specified width."""
    return text.ljust(width, fill_char)

def right_justify(text, width, fill_char=' '):
    """Right justify string within specified width."""
    return text.rjust(width, fill_char)

def pad_left(text, width, pad_char='0'):
    """Pad string on the left to specified width."""
    return text.rjust(width, pad_char)

def pad_right(text, width, pad_char='0'):
    """Pad string on the right to specified width."""
    return text.ljust(width, pad_char)

# Advanced string operations
def longest_word(text):
    """Find the longest word in text."""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def shortest_word(text):
    """Find the shortest word in text."""
    words = text.split()
    if not words:
        return ""
    return min(words, key=len)

def average_word_length(text):
    """Calculate average word length."""
    words = text.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def word_frequency(text):
    """Count frequency of each word (returns dictionary)."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        word = word.strip(string.punctuation)
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def most_frequent_word(text):
    """Find the most frequently occurring word."""
    freq = word_frequency(text)
    if not freq:
        return ""
    return max(freq, key=freq.get)

def least_frequent_word(text):
    """Find the least frequently occurring word."""
    freq = word_frequency(text)
    if not freq:
        return ""
    return min(freq, key=freq.get)

def unique_words(text):
    """Get list of unique words."""
    words = text.lower().split()
    cleaned_words = [word.strip(string.punctuation) for word in words]
    return list(set(cleaned_words))

def count_unique_words(text):
    """Count number of unique words."""
    return len(unique_words(text))

# String validation functions
def is_email(text):
    """Check if string is a valid email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, text))

def is_phone_number(text):
    """Check if string is a valid phone number format."""
    pattern = r'^\+?1?-?\.?\s?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return bool(re.match(pattern, text.strip()))

def is_url(text):
    """Check if string is a valid URL format."""
    pattern = r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w)*)?)$'
    return bool(re.match(pattern, text))

def contains_only_ascii(text):
    """Check if string contains only ASCII characters."""
    try:
        text.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def is_blank(text):
    """Check if string is empty or contains only whitespace."""
    return len(text.strip()) == 0 