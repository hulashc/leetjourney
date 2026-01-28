# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# clarifying questions
# input size - max size of array
# value constraints - integers only, are they negative or zero?
# output guarantees? k<= number of unique elements
# performance expectations?
# edge cases - what if all elements have same frequency? what if k=1?

# Approach 1: Bucket Sort (Optimal)
# Time: O(n), Space: O(n)

def top_k_frequent(nums, k):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Buckets where index = frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


# approach 2: Min-Heap (If asked)
#Time: O(n log k), Space: O(n)

import heapq

def top_k_frequent(nums, k):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]


# Step 3: Edge Cases to Mention

"""
k = 1 → return the most frequent element

All elements unique → any k elements

Negative numbers → works fine

Large input → bucket sort preferred

Multiple elements with same frequency
"""
