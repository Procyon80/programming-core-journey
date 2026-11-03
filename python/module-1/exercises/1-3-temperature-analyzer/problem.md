# Exercise 1.3: Temperature Analyzer

## Problem Statement

Write a program that reads daily temperatures for a week (7 days) and provides statistical analysis.

## Requirements

- Read 7 temperature values from the user (one per line, can be negative)
- Calculate and display:
  1. The highest temperature
  2. The lowest temperature
  3. The average temperature (rounded to 2 decimal places)
  4. Count of days above freezing (> 0°C)
  5. Count of days with extremely hot weather (> 35°C)
  6. Count of days with freezing or below (≤ 0°C)

## Example

**Input:**
```
22
18
-2
15
35
38
20
```

**Output:**
```
--- Daily Temperature Statistics ---
Highest: 38°C
Lowest: -2°C
Average: 20.86°C
Days above freezing: 6
Days extremely hot (>35°C): 2
Days with freezing or below: 1
```

## Requirements

- Do NOT use built-in `max()`, `min()`, or `sum()` functions
- Use loops and conditionals to calculate all values
- Format output clearly with proper rounding
- Handle negative temperatures correctly

## Bonus Challenge

1. Find the temperature change between consecutive days
2. Identify the day with the largest temperature drop/rise
3. Determine if the week was generally cold (<15°C), warm (15-25°C), or hot (>25°C)

## Complexity Analysis

**Time:** O(n) - need to examine each temperature value
**Space:** O(n) - store 7 temperatures in a list

## Testing

Test with edge cases:
- All temperatures the same
- All negative temperatures
- Mix of very hot and very cold days
- Decimal temperatures
