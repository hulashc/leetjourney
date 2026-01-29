

# APPROACH

# brute force - check all substrings - O(n^2)
# optimal(sliding window) - expand right pointer, shrink left pointer when duplicates appear

# DATA STRUCTURES USED - HashSet(or HashMap for last seen index)

# Key invariant - Window [l, r] always containt unique elements

# time complexity -  O(n) time, O(k) space(charset)

"""

"""
c