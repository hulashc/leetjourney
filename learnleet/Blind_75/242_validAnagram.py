# Given two strings s and t, write a function to determine if t is an anagram of s.
# Return True if they are anagrams, else False.

# Constraints
# input size? max length of string? very large?
# char set? lowercase only? or need uppercase? digits? symbols?
# space time constraints? can use extra space? can modify input strings?

# Optimal approach
# Hashmap/frequency counter - O(n) time, O(1) space if inly lower case letters


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}  # Dictionary to count character frequency
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in t:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    return True

# Approach 2: Sorting – O(n log n) time, O(1) space if strings can be sorted in-place

def is_anagram(s,t):
    return sorted(s) == sorted(t)


