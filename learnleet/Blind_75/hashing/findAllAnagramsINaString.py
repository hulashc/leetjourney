




from collections import Counter

def find_anagrams(s, p):
    res = []
    len_p = len(p)
    count_p = Counter(p)
    window = Counter()

    for i, char in enumerate(s):
        window[char] += 1

        # Maintain window size
        if i >= len_p:
            left_char = s[i - len_p]
            if window[left_char] == 1:
                del window[left_char]
            else:
                window[left_char] -= 1

        # Compare window with p
        if window == count_p:
            res.append(i - len_p + 1)

    return res
