# 📖 Module 1.3: Analyzing Efficiency with Big O Notation

## Learning Objectives

By the end of this lesson, you will:
1. Understand what Big O notation measures
2. Analyze the time complexity of your own code
3. Compare different algorithms and choose efficient ones
4. Think algorithmically about problem-solving

---

## 🧮 What is Big O Notation?

**Big O notation** describes how an algorithm's performance **scales with input size**. It answers: "What happens when the input gets 10x bigger?"

### Why It Matters

```python
# Algorithm A: Linear O(n)
def sum_list_naive(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Algorithm B: Quadratic O(n²) - Bad!
def sum_list_terrible(numbers):
    total = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):  # Unnecessary inner loop!
            if i == j:
                total += numbers[j]
    return total
```

**Performance comparison:**
- With 1,000 items: A does 1,000 operations, B does 1,000,000 operations (1,000x slower!)
- With 100,000 items: A does 100,000 operations, B does 10,000,000,000 operations (100,000x slower!)

As the input grows, the difference becomes catastrophic.

---

## 📊 Common Complexities (Best to Worst)

| Complexity | Name | Example | Feasible Input Size |
|---|---|---|---|
| **O(1)** | Constant | Dictionary lookup | Any |
| **O(log n)** | Logarithmic | Binary search | Millions |
| **O(n)** | Linear | Linear search, simple loop | Millions |
| **O(n log n)** | Linearithmic | Merge sort, quick sort | Millions |
| **O(n²)** | Quadratic | Bubble sort, nested loops | Thousands |
| **O(n³)** | Cubic | Triple nested loops | Hundreds |
| **O(2ⁿ)** | Exponential | Generating subsets | < 30 |
| **O(n!)** | Factorial | Generating permutations | < 10 |

---

## 🔍 Analyzing Your Code

### Step 1: Count Loops

```python
# Single loop: O(n)
for i in range(n):
    x = x + 1

# Nested loops: O(n²)
for i in range(n):
    for j in range(n):
        x = x + 1

# Three nested loops: O(n³)
for i in range(n):
    for j in range(n):
        for k in range(n):
            x = x + 1
```

### Step 2: Multiply for Nested Loops

```python
# This is O(n²)
for i in range(n):          # n iterations
    for j in range(n):      # n iterations per outer loop
        print(i, j)         # O(1) operation
# Total: n × n = O(n²)

# This is O(n × m) not O(n²)
for i in range(n):          # n iterations
    for j in range(m):      # m iterations per outer loop
        print(i, j)
# Total: n × m = O(n × m)
```

### Step 3: Drop Constants

```python
# This is O(n) even though it looks like O(3n)
for i in range(n):
    x = x + 1  # First operation
    y = y + 1  # Second operation
    z = z + 1  # Third operation
# We still just loop n times, so it's O(n)

# This is O(n) not O(2n)
for i in range(n):
    print(i)
for i in range(n):
    print(i)
# Total: n + n = 2n = O(n) (we drop the constant 2)
```

### Step 4: Keep Dominant Term

```python
# This is O(n²) not O(n² + n)
for i in range(n):       # O(n)
    for j in range(n):   # O(n) per iteration
        x = x + 1        # O(n²) total

for i in range(n):       # O(n)
    x = x + 1

# Total: n² + n, but n² dominates for large n, so: O(n²)
```

---

## 💡 Common Patterns

### O(1) - Constant Time

Operations that don't depend on input size:

```python
def get_first_element(lst):
    return lst[0]  # Always one operation

def add_two_numbers(a, b):
    return a + b  # Always one operation

# Dictionary lookup
user = users_dict["alice"]  # O(1) regardless of dict size
```

### O(log n) - Logarithmic

Algorithms that cut the problem in half each time:

```python
def binary_search(sorted_list, target):
    """Find target in sorted list - O(log n)"""
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1  # Cut right half
        else:
            right = mid - 1  # Cut left half
    return False
```

**Why logarithmic?**
- 10 items → ~3 iterations
- 100 items → ~7 iterations
- 1,000,000 items → ~20 iterations

### O(n) - Linear

Simple loops over input:

```python
def find_max(lst):
    """Find maximum value - O(n)"""
    max_val = lst[0]
    for item in lst[1:]:
        if item > max_val:
            max_val = item
    return max_val

def sum_elements(lst):
    """Sum all elements - O(n)"""
    total = 0
    for item in lst:
        total += item
    return total
```

### O(n²) - Quadratic

Nested loops:

```python
def bubble_sort(lst):
    """Sort list using bubble sort - O(n²)"""
    n = len(lst)
    for i in range(n):              # O(n)
        for j in range(n - 1):      # O(n)
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def print_all_pairs(lst):
    """Print all pairs - O(n²)"""
    for i in lst:           # n times
        for j in lst:       # n times
            print(i, j)     # n² total
```

### O(n log n) - Linearithmic

Often seen in efficient sorting:

```python
def merge_sort(lst):
    """Sort using merge sort - O(n log n)"""
    # Divide the list into halves (log n levels)
    # At each level, merge all n elements
    # Total: n × log n
    pass
```

### O(2ⁿ) - Exponential

Generally impractical for large inputs:

```python
def fibonacci(n):
    """Recursive fibonacci - O(2ⁿ)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# This does 2^n function calls!
# fibonacci(30) makes over 1,000,000 calls
# fibonacci(50) would take forever
```

---

## 🎯 Practical Application: Choosing Algorithms

**Scenario: Sort 1 million customer records**

- Bubble sort O(n²): ~1 trillion operations (takes minutes)
- Merge sort O(n log n): ~20 million operations (takes milliseconds)

**Scenario: Search for a value in a list of 1 million**

- Linear search O(n): 1 million comparisons worst case
- Binary search O(log n): 20 comparisons worst case (requires sorted list)

---

## 🗄️ Complexity in SQL

SQL engines optimize queries. Big O still applies:

```sql
-- O(n) - Must scan all rows
SELECT * FROM users WHERE last_name = 'Smith';

-- O(log n) - Can use index on user_id
SELECT * FROM users WHERE user_id = 42;

-- O(n²) - Join requires comparing across tables
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.user_id = o.user_id;
```

Indexes make lookups faster (O(log n) instead of O(n)).

---

## ⚠️ Space Complexity

Big O also applies to **memory** usage:

```python
def create_array(n):
    """Creates array of n elements - O(n) space"""
    arr = []
    for i in range(n):
        arr.append(i)
    return arr  # Uses O(n) memory

def in_place_sort(lst):
    """Sorts in-place - O(1) space"""
    # Rearrange lst without creating new arrays
    # Uses only a few temporary variables
    pass
```

**Time vs Space tradeoff:**
- Fast algorithms often use more memory
- Memory-efficient algorithms might be slower
- Choose based on your constraints

---

## 🔢 Exercise 1.5: Complexity Analysis

**Problem:**
Analyze the Big O complexity of each function. Then optimize the slow ones.

**Analyze these functions:**

```python
def func_a(lst):
    """What is the complexity?"""
    result = 0
    for item in lst:
        result += item
    return result

def func_b(lst):
    """What is the complexity?"""
    result = 0
    for item in lst:
        for other in lst:
            if item == other:
                result += 1
    return result

def func_c(lst):
    """What is the complexity?"""
    for i in range(len(lst)):
        for j in range(len(lst)):
            for k in range(len(lst)):
                if lst[i] + lst[j] == lst[k]:
                    print(f"{lst[i]} + {lst[j]} = {lst[k]}")

def func_d(lst):
    """What is the complexity?"""
    result = {}
    for item in lst:
        if item not in result:
            result[item] = 0
        result[item] += 1
    return result
```

**Tasks:**
1. Write the Big O complexity for each
2. Explain your reasoning (count loops, identify dominant term)
3. Optimize func_b to be O(n) instead of O(n²)

---

## ✅ Lesson Checklist

- [ ] I understand Big O notation describes algorithm scaling
- [ ] I can count loops in my code
- [ ] I know the common complexities: O(1), O(log n), O(n), O(n²), O(2ⁿ)
- [ ] I can analyze simple functions and state their complexity
- [ ] I understand why Big O matters for large inputs
- [ ] I understand space complexity as well as time complexity
- [ ] I know some algorithms are better for large inputs
- [ ] I have completed Exercise 1.5

---

## 📚 Reference

For a comprehensive deep-dive, read: `/principles/big-o-notation.md`

## 📖 Next Steps

- Start **Module 2: Data Architecture** for more complex data structures and their complexities
- Or practice by writing your own functions and analyzing their complexity
- Look at the `/sql/module-1/exercises/` for more practice
