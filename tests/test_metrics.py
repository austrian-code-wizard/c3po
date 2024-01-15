import pytest

from src.dataset.feedback import Metric


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
    assert Metric.is_language("Hola, Mundo!", "en") == False
    assert Metric.is_language("Hola, Mundo!", "es") == True


if __name__ == "__main__":
    pytest.main()
