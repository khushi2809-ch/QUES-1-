# Online Exam Result Processor

# Step 1: Input student scores
scores = []
n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input(f"Enter score of student {i+1}: "))
    scores.append(mark)

# Check if enough students
if len(scores) < 3:
    print("Not enough students to remove lowest 2 scores.")
else:
    print("\nOriginal Scores:", scores)

    # Step 2: Remove lowest 2 scores
    scores.sort()
    removed_scores = scores[:2]
    scores = scores[2:]

    print("Removed Lowest 2 Scores:", removed_scores)
    print("Remaining Scores:", scores)

    # Step 3: Add grace marks (5) to those scoring between 30–35
    for i in range(len(scores)):
        if 30 <= scores[i] <= 35:
            scores[i] += 5

    print("Scores After Grace Marks:", scores)

    # Step 4: Count students passed (>= 40)
    passed = 0
    for mark in scores:
        if mark >= 40:
            passed += 1

    print("Number of Students Passed:", passed)

    '''output:
Enter number of students: 5
Enter score of student 1: 28
Enter score of student 2: 32
Enter score of student 3: 45
Enter score of student 4: 38
Enter score of student 5: 25
Original Scores: [28, 32, 45, 38, 25]
Removed Lowest 2 Scores: [25, 28]
Remaining Scores: [32, 38, 45]
Scores After Grace Marks: [37, 38, 45]
Number of Students Passed: 3
    '''
    