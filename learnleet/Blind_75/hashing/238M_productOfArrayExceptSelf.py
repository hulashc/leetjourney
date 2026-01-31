# Given an integer array nums, return an array answer such that
# answer[i] is the product of all elements of nums except nums[i].

#❗ You must solve it in O(n) time and without using division.

# Example - Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# Clarifying questions
# Division allowed?
# Zeros? contains zero? more than 1 zero?
# Input size - what is the maximum size of the array?
# space constraints?

# Optimal Approach (Prefix & Suffix Products)
# Time O(n), space O(1)extra (output array included)

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# no division
# handles 0 naturally

# Edge Cases to Mention
"""
One zero → only that index has non-zero product

Two or more zeros → all outputs are zero

Single element array → [1]

Negative numbers → works fine
"""

