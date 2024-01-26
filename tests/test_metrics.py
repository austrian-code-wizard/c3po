import pytest

from src.dataset.feedback_utils import Metric


def test_length():
    assert Metric.length("Hello, World!", None) == 13
    assert Metric.length("", None) == 0

def test_contains_any_string():
    assert Metric.contains_any_string("Hello, World!", ["Hello", "Python"]) == True
    assert Metric.contains_any_string("Hello, World!", ["Python", "Java"]) == False

def test_contains_all_strings():
    assert Metric.contains_all_strings("Hello, World!", ["Hello", "World"]) == True
    assert Metric.contains_all_strings("Hello, World!", ["Hello", "Python"]) == False

def test_contains_none_strings():
    assert Metric.contains_none_strings("Hello, World!", ["Python", "Java"]) == True
    assert Metric.contains_none_strings("Hello, World!", ["Hello", "Python"]) == False

def test_contains_phone_number():
    assert Metric.contains_phone_number("Call me at (123) 456-7890", "(123) 456-7890") == True
    assert Metric.contains_phone_number("Call me at (123) 456-7890", "(321) 654-0987") == False

def test_ends_with():
    assert Metric.ends_with("Hello, World!", "World!") == True
    assert Metric.ends_with("Hello, World!", "Hello") == False

def test_regex_search():
    assert Metric.regex_search("Hello, World!", r"\bWorld\b") == True
    assert Metric.regex_search("Hello, World!", r"\bPython\b") == False

def test_is_language():
    assert Metric.is_language("Hello, World!", "en") == True
    assert Metric.is_language("Bonjour, Monde!", "en") == False
    assert Metric.is_language("Bonjour, Monde!", "fr") == True

def test_is_length():
    assert Metric.is_length("Hello, World!", 13) == True
    assert Metric.is_length("Hello, World!", 12) == False

def test_first_words():
    assert Metric.first_words("Hello, World!", "Hello") == True
    assert Metric.first_words("Hello, World!", "World") == False

def test_word_count():
    assert Metric.word_count("Hello, World!", 2) == True
    assert Metric.word_count("Hello, World!", 3) == False

def test_word_length():
    assert Metric.word_length_leq("Hello, World!", 5) == True
    assert Metric.word_length_leq("Hello, World!", 4) == False


if __name__ == "__main__":
    pytest.main()
