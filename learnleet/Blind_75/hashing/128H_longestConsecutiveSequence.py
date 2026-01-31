# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input:  [100, 4, 200, 1, 3, 2]
# Output: 4   # sequence is [1, 2, 3, 4]

# clarifying questions
# sorting - is sorting allowed?
# duplicates - can the array contain duplicates
# number range? are they negative or very large?
# input size? whats the max length of the array
# edge cases? can the array be empty?

# Optimal Approach (HashSet)
# time O(n) space O(n)

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            length = 1
            current = num

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

# Example usage
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4
