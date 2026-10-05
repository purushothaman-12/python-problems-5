"""Problem 5: Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating
characters.

Example:
    Input: "abcabcbb"
    Output: 3
"""


def length_of_longest_substring(s):
    """Return the length of the longest substring without repeating chars."""
    seen = {}
    left = 0
    longest = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    tests = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        ""
    ]

    for test in tests:
        print(f"{test!r} -> {length_of_longest_substring(test)}")
