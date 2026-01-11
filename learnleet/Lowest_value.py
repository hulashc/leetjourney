numbers = [10, 4, 7, 2, 9]

lowest = numbers[0]

for num in numbers:
    if num < lowest:
        lowest = num

print("Lowest value in the list is:", lowest)
