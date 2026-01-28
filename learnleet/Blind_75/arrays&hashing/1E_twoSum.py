# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
# Return the answer in any order.

#Constraints
# Input size?
# Integers? negative? zero?
# space constraints?
# multiple pairs summing to target? empty array?

# optimal approach 1: HashMap – O(n) time, O(n) space

def twoSum(nums, target):
    index_map = {}
    for i, num in enumerate(nums):
        complement= target-num
        if complement in index_map:
            return[index_map[complement], i]
        index_map[num]=i
    return[]

# Approach 2: Brute Force – O(n²) time, O(1) space

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
