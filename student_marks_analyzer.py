# Student Marks Analyzer

# Step 1: Input marks
marks = []
n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

# Step 2: Remove invalid marks
valid_marks = []

for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)

# Check if no valid marks
if len(valid_marks) == 0:
    print("No valid marks available.")
else:
    # Step 3: Calculate Average
    average = sum(valid_marks) / len(valid_marks)

    # Step 4: Find Topper(s)
    highest = max(valid_marks)
    toppers = []

    for i in range(len(valid_marks)):
        if valid_marks[i] == highest:
            toppers.append(i + 1)

    # Step 5: Grade based on average
    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Output
    print("\nValid Marks:", valid_marks)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Topper Roll No(s):", toppers)
    print("Class Grade:", grade)
    '''output example:
Enter number of students: 5
Enter marks of student 1: 85
Enter marks of student 2: 92
Enter marks of student 3: 78
Enter marks of student 4: 92
Enter marks of student 5: 45
Valid Marks: [85, 92, 78, 92, 45]
Average Marks: 78.4
Highest Marks: 92
Topper Roll No(s): [2, 4]
Class Grade: A
    '''


    