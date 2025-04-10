from palindrome import is_palindrome


def test_simple_palindrome():
    assert is_palindrome("madam")


def test_mixed_case():
    assert is_palindrome("RaceCar")


def test_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_not_palindrome():
    assert not is_palindrome("hello")


def test_empty_string():
    assert is_palindrome("")
