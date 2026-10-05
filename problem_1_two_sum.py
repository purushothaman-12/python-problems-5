"""Problem 1: Two Sum

Given an array of integers `nums` and an integer `target`, return the indices of
the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
"""


def two_sum(nums, target):
    """Return the indices of the two numbers whose sum is target."""
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
