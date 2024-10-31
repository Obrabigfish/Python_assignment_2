def create_set():
    numbers = input("Enter integers separated by spaces: ")
    return set(map(int, numbers.split()))

print("Enter integers for the first set:")
set1 = create_set()

print("Enter integers for the second set:")
set2 = create_set()
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)

