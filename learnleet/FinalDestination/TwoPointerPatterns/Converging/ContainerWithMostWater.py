






# two pointer converging

def max_area(height):

    left, right = 0, len(height) - 1
    max_area_val = 0

    while left < right:
        area = min(height[left], height(right) * (right - left))
        max_area_val = max(max_area_val, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area_val

# time O(n), space O(1)