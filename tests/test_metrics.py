import pytest
from src.dataset.feedback_utils import Metric


def test_length():
    assert Metric.length("Hello, World!", None) == 13
    assert Metric.length("", None) == 0
    # Test with non-English characters
    assert Metric.length("こんにちは世界", None) == 7


def test_contains_any_string():
    assert Metric.contains_any_string("Hello, World!", ["Hello", "Python"])
    assert not Metric.contains_any_string("Hello, World!", ["Python", "Java"])
    # Case sensitivity test
    assert Metric.contains_any_string("hello, world!", ["Hello"])


def test_contains_all_strings():
    assert Metric.contains_all_strings("Hello, World!", ["Hello", "World"])
    assert not Metric.contains_all_strings("Hello, World!", ["Hello", "Python"])
    # Case sensitivity and partial match test
    assert Metric.contains_all_strings("Hello, World!", ["hello", "world"])


def test_contains_none_strings():
    assert Metric.contains_none_strings("Hello, World!", ["Python", "Java"])
    assert not Metric.contains_none_strings("Hello, World!", ["Hello", "Python"])
    # Case sensitivity test
    assert not Metric.contains_none_strings("Hello, World!", ["hello"])


def test_contains_phone_number():
    assert Metric.contains_phone_number("Call me at (123) 456-7890", "(123) 456-7890")
    assert Metric.contains_phone_number("Call me at 123-456-7890", "(123) 456-7890")
    assert not Metric.contains_phone_number(
        "Call me at (123) 456-7890", "(321) 654-0987"
    )


def test_ends_with():
    assert Metric.ends_with("Hello, World!", "World!")
    assert Metric.ends_with("Hello, World!", "world!")  # Case insensitivity
    assert not Metric.ends_with("Hello, World!", "Hello")


def test_ends_with_cleaned():
    assert Metric.ends_with_cleaned("Hello, World!!", "world!!")
    assert not Metric.ends_with_cleaned("Hello, World!!!", "hello!")
    assert Metric.ends_with_cleaned("Hello,\n  World?", "Hello, world?")


def test_regex_search():
    assert Metric.regex_search("Hello, World!", r"\bWorld\b")
    assert not Metric.regex_search("Hello, World!", r"\bPython\b")


def test_regex_search_false():
    assert not Metric.regex_search_false("Hello, World!", r"\bWorld\b")
    assert Metric.regex_search_false("Hello, World!", r"\bPython\b")


def test_is_language():
    assert Metric.is_language("Hello, World!", "en")
    assert not Metric.is_language("Bonjour, Monde!", "en")
    assert Metric.is_language("Bonjour, Monde!", "fr")


def test_starts_with():
    assert Metric.starts_with("Hello, World!", "Hello")
    assert Metric.starts_with("Hello, World!", "hello")  # Case insensitivity
    assert not Metric.starts_with("Hello, World!", "World")


def test_doesnt_start_with():
    assert Metric.doesnt_start_with("Hello, World!", "World")
    assert not Metric.doesnt_start_with("Hello, World!", "hello")  # Case insensitivity


# Additional tests for other metrics if they exist

if __name__ == "__main__":
    pytest.main()
