# 🧮 Big O Notation: Understanding Algorithm Efficiency

## Introduction

Big O notation is the language we use to talk about **how an algorithm's runtime or space requirements grow as the input size increases**. It abstracts away constant factors and focuses on the dominant pattern of growth, allowing us to compare algorithms on a fundamental level.

Why does this matter? Because the difference between O(n) and O(n²) can mean the difference between a program finishing in seconds versus taking hours—especially as data scales.

## The Big O Family

### O(1) - Constant Time
The operation takes the same amount of time regardless of input size.

**Examples:**
- Accessing an element in a list by index: `arr[5]`
- Looking up a key in a dictionary: `dict['key']`
- Incrementing a variable
- Checking if a number is even: `n % 2 == 0`

**Code Pattern:**
```python
def get_first_element(lst):
    return lst[0]  # Always one operation, no matter how big lst is
```

**Visualization:**
```
Time
  |
  | -------
  |       |
  |-------|----------- Input Size
```

The line is flat—growth doesn't increase with input.

### O(log n) - Logarithmic Time
The algorithm cuts the problem in half each iteration.

**Examples:**
- Binary search: checking a sorted list for a value by repeatedly cutting the search space in half
- Finding an element in a balanced binary tree
- Calculating log₂(1,000,000) = ~20 iterations

**Why is it logarithmic?**
```
Input: 1,000,000 items
After 1st iteration: 500,000 items remain
After 2nd iteration: 250,000 items remain
After 3rd iteration: 125,000 items remain
...
After 20th iteration: 1 item remains
```

**Code Pattern:**
```python
def binary_search(sorted_lst, target):
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_lst[mid] == target:
            return True
        elif sorted_lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

### O(n) - Linear Time
The time grows proportionally with the input size.

**Examples:**
- Searching through a list to find a value (linear search)
- Summing all elements in an array
- Printing each element in a list

**Code Pattern:**
```python
def find_max(lst):
    max_val = lst[0]
    for item in lst:  # We look at every item once
        if item > max_val:
            max_val = item
    return max_val
```

**Analysis:** If the list has 1,000 items, we do ~1,000 comparisons. If it has 10,000 items, we do ~10,000 comparisons.

### O(n log n) - Linearithmic Time
A hybrid of linear and logarithmic—common in efficient sorting algorithms.

**Examples:**
- Merge sort
- Quick sort (average case)
- Most built-in sorting functions

**Intuition:** Think of it as doing a logarithmic amount of work on each of the n items.

### O(n²) - Quadratic Time
The algorithm has nested loops over the input.

**Examples:**
- Bubble sort
- Selection sort
- Naive string matching (comparing every substring)
- Nested loops checking all pairs

**Code Pattern:**
```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):          # Outer loop: n times
        for j in range(n - 1):  # Inner loop: n-1 times
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
```

**Analysis:** With 10 items, we do ~100 comparisons. With 100 items, we do ~10,000 comparisons. This grows quickly!

### O(2ⁿ) - Exponential Time
The algorithm's complexity doubles with each additional item.

**Examples:**
- Recursive Fibonacci (naive implementation)
- Generating all subsets of a set
- Brute-force solving of the traveling salesman problem

**Code Pattern:**
```python
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
    # For n=30, we make 2,000,000+ function calls!
```

**Analysis:** This complexity is generally considered unacceptable for large inputs. At n=50, you might wait forever.

### O(n!) - Factorial Time
Even worse than exponential—the work multiplies with each additional item.

**Examples:**
- Generating all permutations of a list
- Brute-force solving of certain combinatorial problems

**Code Pattern:**
```python
def generate_permutations(lst):
    if len(lst) == 1:
        return [lst]
    perms = []
    for i, item in enumerate(lst):
        remaining = lst[:i] + lst[i+1:]
        for perm in generate_permutations(remaining):
            perms.append([item] + perm)
    return perms
```

## Comparing Complexities

Here's how they scale with input size:

| Input Size | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|---|---|---|---|---|---|
| 10 | 1 | 3 | 10 | 33 | 100 | 1,024 |
| 100 | 1 | 7 | 100 | 664 | 10,000 | 2^100 ≈ huge |
| 1,000 | 1 | 10 | 1,000 | 9,966 | 1,000,000 | 2^1000 ≈ impossible |
| 1,000,000 | 1 | 20 | 1,000,000 | 20,000,000 | 1,000,000,000,000 | - |

**Key insight:** As input grows, polynomial algorithms (O(n), O(n²)) remain feasible. Exponential algorithms become infeasible very quickly.

## Space Complexity

Big O also applies to **space** (memory) requirements:

- **O(1)**: Constant extra space (e.g., a few variables)
- **O(n)**: Space proportional to input (e.g., creating a new list of same size)
- **O(n²)**: Space for a 2D grid or matrix of input size

## How to Calculate Big O

### Step 1: Count Operations
Look at loops and how many times they execute.

```python
def example(lst):
    x = 0           # O(1) - constant
    for item in lst:  # O(n) - runs n times
        x += item
    return x
```

Overall: O(1) + O(n) = **O(n)** (drop constants)

### Step 2: Handle Nested Loops
Multiply the complexities.

```python
def nested_example(lst):
    for i in lst:        # n times
        for j in lst:    # n times
            print(i, j)  # O(1)
```

Overall: O(n) × O(n) = **O(n²)**

### Step 3: Handle Sequential Operations
Add the complexities, but keep the dominant term.

```python
def sequential(lst):
    for i in lst:          # O(n)
        print(i)
    for i in lst:          # O(n)
        for j in lst:      # O(n)
            print(i, j)
```

Overall: O(n) + O(n²) = **O(n²)** (n² dominates)

### Step 4: Drop Constants
Big O ignores constant multipliers.

```python
for i in range(n):       # n iterations
    print(i)
    print(i)
    print(i)            # 3n operations, but still O(n)
```

We write **O(n)**, not O(3n).

## Practical Implications

**Choose algorithms wisely based on expected input size:**

- **Small data (< 1,000 items):** O(n²) is usually fine
- **Medium data (1,000 - 1,000,000):** Use O(n) or O(n log n)
- **Large data (> 1,000,000):** Use O(n) or O(log n); avoid O(n²) and above
- **Real-time systems:** O(1) and O(log n) preferred

**Remember:** A poorly implemented O(n log n) algorithm can be slower than a well-implemented O(n²) on small inputs due to constants. But as n grows, Big O always wins in the end.

## Key Takeaways

1. **Big O describes the dominant growth pattern** of an algorithm
2. **Not all O(n) algorithms are equal**, but they scale similarly
3. **Exponential and factorial complexities are impractical** for most real-world problems
4. **Knowing Big O helps you write scalable code** and choose the right tool for the job
5. **Always consider both time AND space complexity** when evaluating algorithms
