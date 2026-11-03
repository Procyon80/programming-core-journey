# Exercise 1.1: Find the Maximum Value - Solution

# Read 5 numbers from the user and store in a list
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input())  # float() allows decimals and integers
    numbers.append(num)

# Find the maximum value (without using max())
max_value = numbers[0]  # Start with the first number
max_index = 0           # Track the index

for i in range(1, len(numbers)):  # Start from index 1
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i

# Print the results
print(f"The maximum value is: {max_value}")
print(f"It is at index: {max_index}")

# Bonus: Also find minimum and average
min_value = numbers[0]
min_index = 0

for i in range(1, len(numbers)):
    if numbers[i] < min_value:
        min_value = numbers[i]
        min_index = i

average = sum(numbers) / len(numbers)

print(f"\nBonus Information:")
print(f"The minimum value is: {min_value}")
print(f"It is at index: {min_index}")
print(f"The average is: {average:.2f}")

# Count numbers above average
above_average_count = 0
for num in numbers:
    if num > average:
        above_average_count += 1

print(f"Numbers above average: {above_average_count}")

# Complexity Analysis:
# Time Complexity: O(n) - we loop through the list once to find the max
# Space Complexity: O(n) - we store n numbers in the list
