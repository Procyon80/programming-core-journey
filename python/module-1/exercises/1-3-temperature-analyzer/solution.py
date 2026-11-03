# Exercise 1.3: Temperature Analyzer - Solution

# Read 7 temperatures and store in a list
temperatures = []
print("Enter 7 daily temperatures:")
for i in range(7):
    temp = float(input())
    temperatures.append(temp)

# Calculate highest temperature
highest = temperatures[0]
for temp in temperatures:
    if temp > highest:
        highest = temp

# Calculate lowest temperature
lowest = temperatures[0]
for temp in temperatures:
    if temp < lowest:
        lowest = temp

# Calculate average temperature
total = 0
for temp in temperatures:
    total += temp
average = total / len(temperatures)

# Count days above freezing (> 0)
above_freezing = 0
for temp in temperatures:
    if temp > 0:
        above_freezing += 1

# Count days extremely hot (> 35)
extremely_hot = 0
for temp in temperatures:
    if temp > 35:
        extremely_hot += 1

# Count days freezing or below (<= 0)
freezing_or_below = 0
for temp in temperatures:
    if temp <= 0:
        freezing_or_below += 1

# Display results
print("\n--- Daily Temperature Statistics ---")
print(f"Highest: {highest}°C")
print(f"Lowest: {lowest}°C")
print(f"Average: {average:.2f}°C")
print(f"Days above freezing: {above_freezing}")
print(f"Days extremely hot (>35°C): {extremely_hot}")
print(f"Days with freezing or below: {freezing_or_below}")

# Bonus: Temperature changes
print("\n--- Bonus: Daily Changes ---")
for i in range(1, len(temperatures)):
    change = temperatures[i] - temperatures[i-1]
    direction = "up" if change > 0 else "down"
    print(f"Day {i} to Day {i+1}: {change:+.1f}°C ({direction})")

# Bonus: Overall assessment
average_temp = average
if average_temp < 15:
    assessment = "generally cold"
elif average_temp <= 25:
    assessment = "warm"
else:
    assessment = "hot"

print(f"\nWeek Assessment: The week was {assessment} (avg {average_temp:.1f}°C)")
