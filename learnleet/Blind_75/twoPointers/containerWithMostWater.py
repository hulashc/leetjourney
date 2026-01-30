

# You are given an integer array height where each element represents the height of a vertical line at that index.
# Find two lines that together with the x-axis form a container that holds the most water, and return its area.
# You may not slant the container.

def max_area(heights):

    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        area = min(heights[left], heights[right]) * width
        max_area = max(max_area, area)
        
        if heights[left] < heights[right]:
            left +=1
        else:
            right -+1
    
    return max_area


