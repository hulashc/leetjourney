def mergeAlternately(s1: str, s2: str) -> str:
    result = []
    i, j = 0, 0
    # Loop until both strings are fully processed
    while i < len(s1) or j < len(s2):
        if i < len(s1):  # If there are still characters in s1
            result.append(s1[i])
            i += 1
        if j < len(s2):  # If there are still characters in s2
            result.append(s2[j])
            j += 1
    return ''.join(result)

# Test cases
s1 = "abc"
s2 = "defgh"
print(mergeAlternately(s1, s2))  # Output: "adbcefg"

