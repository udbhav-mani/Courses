from collections import Counter

numbers = [1, 2, 1, 3, 5, 3, 6, 4, 4, 2, 7, 8, 9, 4, 8, 3, 3, 6, 8, 2]
counter = Counter(numbers)
print(counter[3])
print(counter[35])
print(counter)
