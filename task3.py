

def is_closed(str: str):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in str:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack


if __name__ == "__main__":

    assert is_closed("()") is True

    assert is_closed("(){}[]") is True

    assert is_closed("([{}])") is True

    assert is_closed("((()))") is True

    assert is_closed(")") is False

    assert is_closed("([)]") is False

    assert is_closed("{") is False

    assert is_closed("") is True

    assert is_closed("{[()]}") is True

    assert is_closed("{[()]}()") is True
