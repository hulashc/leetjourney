


# reverse the whole array, then reverse k elements, then reverse remaining elements

def rotate(nums, k):
    n = len(nums)
    k %= n  # handle k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # 1. Reverse entire array
    reverse(0, n-1)
    # 2. Reverse first k elements
    reverse(0, k-1)
    # 3. Reverse remaining elements
    reverse(k, n-1)
