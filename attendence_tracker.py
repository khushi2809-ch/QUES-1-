# Attendance Tracker

# Step 1: Input attendance
attendance = []
n = int(input("Enter number of days: "))

for i in range(n):
    status = int(input(f"Day {i+1} (1 = Present, 0 = Absent): "))
    attendance.append(status)

# Step 2: Calculate attendance percentage
total_present = attendance.count(1)
percentage = (total_present / n) * 100

print("\nAttendance Percentage:", percentage, "%")

# Step 3: Check if below 75%
if percentage < 75:
    print("Student is below 75% attendance.")
else:
    print("Attendance is satisfactory.")

# Step 4: Replace consecutive absences with warning flag
warning_attendance = attendance.copy()

for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        warning_attendance[i] = "⚠"
        warning_attendance[i+1] = "⚠"

print("Attendance with Warning Flags:", warning_attendance)

''' output example:
Enter number of days: 10
Day 1 (1 = Present, 0 = Absent): 1
Day 2 (1 = Present, 0 = Absent): 0
Day 3 (1 = Present, 0 = Absent): 0
Day 4 (1 = Present, 0 = Absent): 1
Day 5 (1 = Present, 0 = Absent): 1
Day 6 (1 = Present, 0 = Absent): 0
Day 7 (1 = Present, 0 = Absent): 1
Day 8 (1 = Present, 0 = Absent): 1
Day 9 (1 = Present, 0 = Absent): 0
Day 10 (1 = Present, 0 = Absent): 1
Attendance Percentage: 70.0 %
Student is below 75% attendance.
Attendance with Warning Flags: [1, '⚠', '⚠', 1, 1, 0, 1, 1, 0, 1]
'''
