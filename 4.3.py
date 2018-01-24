# 4-3
# for value in range(1, 20):
#     print(value)

# 4-4
# numbers = list(range(1, 1000001))
# for i in range(1, 1000000):
#     print(numbers[i])


# 4-5
# nums = list(range(1, 1000001))
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# 4-6
# odds = list(range(1, 20, 2))
# print(odds)

# 4-7
# numbers = list(range(3, 30, 3))
# for number in numbers:
#     print(number)

# 4-8
# triple = []
# for i in range(1, 11):
#     value = i ** 3
#     triple.append(value)
# for i in range(0, 10):
#     print(triple[i])

# 4-9
triple = [num**3 for num in range(1, 11)]
print(triple)
