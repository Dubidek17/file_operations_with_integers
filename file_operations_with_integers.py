number_of_elements = 0
mean = 0
numbers_greater_than_mean = 0
numbers = []

with open("numbers.txt") as file:
    for row in file:
        numbers.append(int(row))

maximum_value = numbers[0]
minimum_value = numbers[0]
for number in numbers:
    number_of_elements += 1
    mean += number
    if number > maximum_value:
        maximum_value = number
    if number < minimum_value:
        minimum_value = number
mean = mean / len(numbers)

for number in numbers:
    if number > mean:
        numbers_greater_than_mean += 1


print(f"Number of elements: {number_of_elements}")
print(f"Maximum value: {maximum_value}")
print(f"Minimum value: {minimum_value}")
print(f"Mean: {mean}")
print(f"Numbers greater than the mean: {numbers_greater_than_mean}")