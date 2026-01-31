def min_window(s, t):
    if not t or not s:
        return ""

    from collections import Counter

    need = Counter(t)
    window = {}

    left = 0
    formed = 0
    required = len(need)

    res_len = float("inf")
    res = (0, 0)

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < res_len:
                res_len = right - left + 1
                res = (left, right)

            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1

    l, r = res
    return "" if res_len == float("inf") else s[l:r+1]
