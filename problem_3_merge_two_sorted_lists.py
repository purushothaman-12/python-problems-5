"""Problem 3: Merge Two Sorted Lists

You are given two sorted arrays `nums1` and `nums2` of size `m` and `n`
respectively. Merge them into one sorted array.

Example:
    Input: nums1 = [1, 2, 3], nums2 = [2, 5, 6]
    Output: [1, 2, 2, 3, 5, 6]
"""


def merge_sorted_lists(nums1, nums2):
    """Merge two sorted arrays into one sorted array."""
    merged = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    return merged


if __name__ == "__main__":
    print(merge_sorted_lists([1, 2, 3], [2, 5, 6]))
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
