"""Problem 2: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into
lowercase and removing all non-alphanumeric characters, it reads the same
forward and backward.

Example:
    Input: "A man, a plan, a canal: Panama"
    Output: True
"""


def is_palindrome(s):
    """Return True if the string is a palindrome after cleaning it."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    tests = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " "
    ]

    for test in tests:
        print(f"{test!r} -> {is_palindrome(test)}")
