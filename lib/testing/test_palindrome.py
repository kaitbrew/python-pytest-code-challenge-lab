import pytest
from palindrome import longest_palindromic_substring


def test_longest_palindromic_substring_basic_cases():
    assert longest_palindromic_substring("babad") in {"bab", "aba"}
    assert longest_palindromic_substring("cbbd") == "bb"


def test_longest_palindromic_substring_single_and_double_chars():
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("ac") in {"a", "c"}


def test_longest_palindromic_substring_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_no_repeating_chars_returns_one_char():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1
    assert result in set("abcde")


def test_even_length_palindrome():
    inp = "forgeeksskeegfor"
    assert longest_palindromic_substring(inp) == "geeksskeeg"


def test_all_same_chars():
    s = "aaaaa"
    assert longest_palindromic_substring(s) == s