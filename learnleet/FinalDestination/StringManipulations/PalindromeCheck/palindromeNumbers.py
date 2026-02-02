


# Optimal Approach (Math, No String) ⭐
# 🔑 Key Insight

# You only need to reverse half of the number.

# Why?

# Reversing the full number risks overflow (in other languages)

# Half-reversal is faster and cleaner

def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Handles both even & odd length numbers
    return x == reversed_half or x == reversed_half // 10




# Simple string based solutions

def is_palindrome(x):
    return str(x) == str(x)[::-1]
