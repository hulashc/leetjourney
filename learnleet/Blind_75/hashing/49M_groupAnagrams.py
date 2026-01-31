# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.


# Example
# Input: ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

# Clarifying questions
# input size, max no. of stings, max length of string
# char constraints - lowercase only or uppercase, digits etc?
# space constraints? extra space allowed for hashmaps?
# edge cases - can the input be empty? can strings be empty ("")?

# approach 1: Character Count (O(n · k))
# where n = number of strings, k = max length of a string

def group_anagrams(strs):
    anagrams = {}  # key -> list of words

    for word in strs:
        count = [0] * 26  # assuming lowercase letters
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        key = tuple(count)  # lists can't be dict keys
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    return list(anagrams.values())




# approach 2: Sorting (Simpler, but slower) - Time: O(n · k log k), acceptable unless large strings

def group_anagrams(strs):
    anagrams = {}

    for word in strs:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    return list(anagrams.values())


# Step 3: Edge Cases to Mention
"""
Empty input → []

Single string → [[word]]

Empty strings → ["", ""] → [["", ""]]

All strings unique → each in its own group

Very long strings → frequency approach preferred
"""