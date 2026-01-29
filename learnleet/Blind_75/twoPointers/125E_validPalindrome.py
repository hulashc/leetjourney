

# string - s, return true if palindrome, other return false

def palinfrome(alfnum):
    if alfnum == alfnum[::-1]:
        return True
    return False


list = [1,2,3,4]


def is_palindrome(list):

    l, r = 0, len(list) - 1

    while l < r:

        while l < r and not list[l].alnum():
            left += 1
        while l < r and not list[r].alnum():
            right -= 1

        if list[l].lower() != list[r].lower():
            return False
    
        l += 1
        r -= 1
    return True


    