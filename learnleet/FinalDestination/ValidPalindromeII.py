




# two pointers method

def valid_palindrome(s):
    def is_pal(l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            return True
        
        left , right = 0 , len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return 
            