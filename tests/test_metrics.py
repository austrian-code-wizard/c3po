import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langdetect import detect  # Assuming langdetect is used for language detection
from src.dataset.feedback_utils import Metric


def test_length():
    assert Metric.length("Hello, World!", None) == 13
    assert Metric.length("", None) == 0
    # Test with non-English characters
    assert Metric.length("こんにちは世界", None) == 7

def test_contains_any_string():
    assert Metric.contains_any_string("Hello, World!", ["Hello", "Python"]) == True
    assert Metric.contains_any_string("Hello, World!", ["Python", "Java"]) == False
    # Case sensitivity test
    assert Metric.contains_any_string("hello, world!", ["Hello"]) == True

def test_contains_all_strings():
    assert Metric.contains_all_strings("Hello, World!", ["Hello", "World"]) == True
    assert Metric.contains_all_strings("Hello, World!", ["Hello", "Python"]) == False
    # Case sensitivity and partial match test
    assert Metric.contains_all_strings("Hello, World!", ["hello", "world"]) == True

def test_contains_none_strings():
    assert Metric.contains_none_strings("Hello, World!", ["Python", "Java"]) == True
    assert Metric.contains_none_strings("Hello, World!", ["Hello", "Python"]) == False
    # Case sensitivity test
    assert Metric.contains_none_strings("Hello, World!", ["hello"]) == False

def test_contains_phone_number():
    assert Metric.contains_phone_number("Call me at (123) 456-7890", "(123) 456-7890") == True
    assert Metric.contains_phone_number("Call me at 123-456-7890", "(123) 456-7890") == True
    assert Metric.contains_phone_number("Call me at (123) 456-7890", "(321) 654-0987") == False

def test_ends_with():
    assert Metric.ends_with("Hello, World!", "World!") == True
    assert Metric.ends_with("Hello, World!", "world!") == True  # Case insensitivity
    assert Metric.ends_with("Hello, World!", "Hello") == False

def test_ends_with_cleaned():
    assert Metric.ends_with_cleaned("Hello, World!!", "world!!") == True
    assert Metric.ends_with_cleaned("Hello, World!!!", "hello!") == False
    assert Metric.ends_with_cleaned("Hello,\n  World?", "Hello, world?") == True

def test_regex_search():
    assert Metric.regex_search("Hello, World!", r"\bWorld\b") == True
    assert Metric.regex_search("Hello, World!", r"\bPython\b") == False

def test_regex_search_false():
    assert Metric.regex_search_false("Hello, World!", r"\bWorld\b") == False
    assert Metric.regex_search_false("Hello, World!", r"\bPython\b") == True

def test_is_language():
    assert Metric.is_language("Hello, World!", "en") == True
    assert Metric.is_language("Bonjour, Monde!", "en") == False
    assert Metric.is_language("Bonjour, Monde!", "fr") == True

def test_starts_with():
    assert Metric.starts_with("Hello, World!", "Hello") == True
    assert Metric.starts_with("Hello, World!", "hello") == True  # Case insensitivity
    assert Metric.starts_with("Hello, World!", "World") == False

def test_doesnt_start_with():
    assert Metric.doesnt_start_with("Hello, World!", "World") == True
    assert Metric.doesnt_start_with("Hello, World!", "hello") == False  # Case insensitivity

def test_sentiment():
    assert Metric.sentiment("I love this product! It's amazing!", 0.1) == True
    assert Metric.sentiment("This is fantastic and wonderful!", 0.0) == True
    assert Metric.sentiment("I hate this terrible product!", 0.0) == False
    assert Metric.sentiment("I hate this terrible product!", -0.95) == True
    assert Metric.sentiment("This is a product.", 0.0) == True
    assert Metric.sentiment("The item arrived on time.", -0.1) == True

# Additional tests for other metrics if they exist

if __name__ == "__main__":
    test_functions = [
        test_length,
        test_contains_any_string,
        test_contains_all_strings,
        test_contains_none_strings,
        test_contains_phone_number,
        test_ends_with,
        test_ends_with_cleaned,
        test_regex_search,
        test_regex_search_false,
        test_is_language,
        test_starts_with,
        test_doesnt_start_with,
        test_sentiment
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__} passed")
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__} failed: {e}")
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    exit(0 if failed == 0 else 1)
