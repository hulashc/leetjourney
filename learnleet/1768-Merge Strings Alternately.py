def mergeAlternately(w1, w2):
    result = []
    i = 0

    while i < len(w1) or i < len(w2):
        if i < len(w1):
            result.append(w1[i])
        if i < len(w2):
            result.append(w2[i])
        i += 1

    return "".join(result)