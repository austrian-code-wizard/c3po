import pytest
import re
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

def test_sentiment_polarity():
    positive_text = "I love this amazing product! It's fantastic and wonderful!"
    positive_score = Metric.sentiment_polarity(positive_text, None)
    assert positive_score > 0, f"Expected positive sentiment, got {positive_score}"
    
    negative_text = "I hate this terrible product. It's awful and disappointing."
    negative_score = Metric.sentiment_polarity(negative_text, None)
    assert negative_score < 0, f"Expected negative sentiment, got {negative_score}"
    
    neutral_text = "This is a product. It exists."
    neutral_score = Metric.sentiment_polarity(neutral_text, None)
    assert -0.1 <= neutral_score <= 0.1, f"Expected neutral sentiment, got {neutral_score}"
    
    assert isinstance(positive_score, float), "Sentiment polarity should return a float"
    
    assert -1 <= positive_score <= 1, f"Sentiment score should be between -1 and 1, got {positive_score}"
    assert -1 <= negative_score <= 1, f"Sentiment score should be between -1 and 1, got {negative_score}"

# Additional tests for other metrics if they exist

if __name__ == "__main__":
    pytest.main()
