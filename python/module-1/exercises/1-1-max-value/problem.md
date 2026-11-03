# Exercise 1.1: Find the Maximum Value

## Problem Statement

Write a Python script that takes a list of numbers and finds the maximum value **without using the built-in `max()` function**.

## Requirements

- Read 5 numbers from user input (one number per line)
- Store them in a list
- Find and print the maximum value
- Print the index (position) of the maximum value
- Verify your solution works for negative numbers and decimals

## Example

**Input:**
```
10
5
23
15
8
```

**Output:**
```
The maximum value is: 23
It is at index: 2
```

## Edge Cases to Consider

- What if all numbers are the same?
- What if all numbers are negative?
- What if there are decimal numbers?
- What if the maximum value appears multiple times?

## Bonus Challenge

After solving the basic problem:
1. Modify the script to also find the minimum value
2. Calculate the average of all numbers
3. Count how many numbers are above the average
4. Analyze the Big O complexity of your solution

## Expected Complexity

**Time:** O(n) - we must examine each element once to find the maximum
**Space:** O(n) - we store all n numbers in the list

## Testing Your Solution

Test with these cases:
```python
# Test 1: Mixed positive numbers
[10, 5, 23, 15, 8] → max=23, index=2

# Test 2: Negative numbers
[-5, -2, -10, -1] → max=-1, index=3

# Test 3: Decimals
[3.5, 2.1, 4.8, 1.2] → max=4.8, index=2

# Test 4: Single value repeated
[5, 5, 5, 5] → max=5, index=0
```
