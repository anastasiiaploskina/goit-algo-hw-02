import re
from collections import deque


def is_palindrome(text: str):
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

    d = deque(clean_text)

    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


if __name__ == "__main__":

    assert is_palindrome("radar") is True

    assert is_palindrome("level") is True

    assert is_palindrome("python") is False

    assert is_palindrome("") is True

    assert is_palindrome("a") is True

    assert is_palindrome("Madam") is True

    assert is_palindrome("racecar") is True

    assert is_palindrome("A man, a plan, a canal: Panama") is True

    assert is_palindrome("12321") is True

    assert is_palindrome("not a palindrome") is False
