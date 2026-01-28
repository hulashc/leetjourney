# Given a list of integers nums, return True if any value appears at least twice in the list, 
# and False if every element is distinct.

# Optimal approach (Hashset) - O(n) time, O(n) space.


# Questions to ask
# Ask about input size(small or millions)
# Ask about value range(integers? negatives? duplicates frequent or rare?)
# Ask space constraints? (yes? then use sorting, no? then use Hashmap)


'''
Explanation:

Use a set to keep track of numbers we have seen.

Iterate through the list:

If the number is already in the set → duplicate found → return True.

Else, add it to the set.

If the loop ends without finding duplicates → return False.

Why this is Goldman-level:

Efficiency: Linear time, minimal extra space.

Clarity: Easy to reason about.

Readability: Uses built-in Python types, no unnecessary imports.
'''


def contains_duplicate(nums):
    seen = set()  # To track seen numbers
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)
    return False  # No duplicates found

# Example usage
nums = [3, 1, 4, 2, 5, 3]
print(contains_duplicate(nums))  # Output: True


# Optional Follow-Up (If asked for O(1) extra space):
# You can sort the array first and then check adjacent elements.
# Time: O(n log n), Space: O(1) if sorting in-place.

def contains_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False










