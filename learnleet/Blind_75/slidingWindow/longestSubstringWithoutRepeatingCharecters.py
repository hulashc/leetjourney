

# APPROACH

# brute force - check all substrings - O(n^2)
# optimal(sliding window) - expand right pointer, shrink left pointer when duplicates appear

# DATA STRUCTURES USED - HashSet(or HashMap for last seen index)

# Key invariant - Window [l, r] always containt unique elements

# time complexity -  O(n) time, O(k) space(charset)

"""

"""

def longstring(s):

    char_index = {}
    left = 0
    max_length = 0
    
    
    for right in range(len(s)):
        if s[right]  in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

