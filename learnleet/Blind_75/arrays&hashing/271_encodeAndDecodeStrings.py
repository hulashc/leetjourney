# Design an algorithm to encode a list of strings into a single string.
# The encoded string should be decoded back to the original list of strings.
# Example
# Input: ["lint","code","love","you"]
# Encoded: "4#lint4#code4#love3#you"
# Decoded: ["lint","code","love","you"]

# Clarifying questions
# charecter constraints = can strings contain any charecters, including #,numbers or symbols? or be empty
# encoding format - any restrictions? encoded string human readable?
# performance - max number of string, max length of the strings
# storage/transport - should encoding be space sufficient?

# Optimal Approach (Length-Prefixed Encoding)
# Use length + delimiter + string for each word.

#ENCODE
def encode(strs):
    encoded = ""
    for s in strs:
        encoded += str(len(s)) + "#" + s
    return encoded

#DECODE
def decode(s):
    result = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        word = s[j + 1 : j + 1 + length]
        result.append(word)

        i = j + 1 + length

    return result

# Edge Cases (Say These Out Loud)
"""
Empty list → []

List with empty strings → ["", ""]

Strings containing # → "a#b" (works correctly)

Very long strings

Single string
"""