# Temperature Monitoring System

# Step 1: Input daily temperatures
temps = []
n = int(input("Enter number of days: "))

for i in range(n):
    t = float(input(f"Enter temperature for Day {i+1}: "))
    temps.append(t)

print("\nOriginal Temperatures:", temps)

# Step 2: Find hottest and coldest day
max_temp = max(temps)
min_temp = min(temps)

hottest_day = temps.index(max_temp) + 1
coldest_day = temps.index(min_temp) + 1

print("Hottest Day: Day", hottest_day, "with", max_temp, "°C")
print("Coldest Day: Day", coldest_day, "with", min_temp, "°C")

# Step 3: Replace temperatures above 45°C with "Heat Alert"
updated_temps = temps.copy()

for i in range(len(updated_temps)):
    if updated_temps[i] > 45:
        updated_temps[i] = "Heat Alert"

print("After Heat Alert Update:", updated_temps)

# Step 4: Count extreme days (> 40°C)
extreme_count = 0

for t in temps:
    if t > 40:
        extreme_count += 1

print("Number of Extreme Days (>40°C):", extreme_count)

''' output example:
Enter number of days: 5
Enter temperature for Day 1: 30
Enter temperature for Day 2: 42
Enter temperature for Day 3: 38
Enter temperature for Day 4: 46
Enter temperature for Day 5: 41
Original Temperatures: [30.0, 42.0, 38.0, 46.0, 41.0]
Hottest Day: Day 4 with 46.0 °C
Coldest Day: Day 1 with 30.0 °C
After Heat Alert Update: [30.0, 42.0, 38.0, 'Heat Alert', 41.0]
Number of Extreme Days (>40°C): 3
'''

