import pytest
import re
from langdetect import detect  # Assuming langdetect is used for language detection
from src.dataset.feedback_utils import Metric, Comparison


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

def test_metric_call():
    # Test that __call__ delegates to the value function
    assert Metric.length("Hello, World!", None) == Metric.length.value("Hello, World!", None)
    # Test with different metric types
    assert Metric.contains_any_string("Hello", ["Hello", "World"]) == Metric.contains_any_string.value("Hello", ["Hello", "World"])
    assert Metric.is_language("Hello", "en") == Metric.is_language.value("Hello", "en")

def test_comparison_call():
    # Test greater_eq_than comparison
    assert Comparison.greater_eq_than(5, 6) == True  # 5 <= 6
    assert Comparison.greater_eq_than(6, 5) == False  # 6 <= 5
    assert Comparison.greater_eq_than(5, 5) == True  # 5 <= 5
    
    # Test less_eq_than comparison
    assert Comparison.less_eq_than(5, 6) == False  # 5 >= 6
    assert Comparison.less_eq_than(6, 5) == True  # 6 >= 5
    assert Comparison.less_eq_than(5, 5) == True  # 5 >= 5

# Additional tests for other metrics if they exist

if __name__ == "__main__":
    pytest.main()
