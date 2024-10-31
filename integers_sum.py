numbers_list = []
total = 0
numbers = input("Enter a list of integers: ")
for i in numbers:
    numbers_list = list(numbers)
    total += int(i)
print(numbers_list)
print(total)
