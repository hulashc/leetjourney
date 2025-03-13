## Contains Duplicate
# EASY
# Given an integer array [nums], return [true] if any value appears more than once in the array, otherwise return [false].
# 

List = [1,2,3,4]

#Brute Force

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: # type: ignore
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


#Sorting

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: # type: ignore
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

#Hash Set

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set