numbers = [3, 5, 6, 8, 9, 12, 14, 15]

result = list(filter(lambda x: x % 3 == 0, numbers))

print("Numbers divisible by 3:", result)
