# Sports Tournament Points Table

# Step 1: Input team points
points = []
n = int(input("Enter number of teams: "))

for i in range(n):
    p = int(input(f"Enter points of Team {i+1}: "))
    points.append(p)

print("\nOriginal Points:", points)

# Step 2: Replace negative points with 0
for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0

print("After Replacing Negative Points:", points)

# Step 3: Sort leaderboard (descending)
points.sort(reverse=True)
print("Sorted Leaderboard (High to Low):", points)

# Step 4: Find winner and runner-up
if len(points) >= 2:
    winner = points[0]
    runner_up = points[1]

    print("Winner Points:", winner)
    print("Runner-up Points:", runner_up)
elif len(points) == 1:
    print("Only one team. Winner Points:", points[0])
else:
    print("No teams available.")

    '''output:
    Enter number of teams: 5
    Enter points of Team 1: 10
    Enter points of Team 2: -5
    Enter points of Team 3: 15
    Enter points of Team 4: 20
    Enter points of Team 5: 8
    Original Points: [10, -5, 15, 20, 8]
    After Replacing Negative Points: [10, 0, 15, 20, 8]
    Sorted Leaderboard (High to Low): [20, 15, 10, 8, 0]
    Winner Points: 20
    Runner-up Points: 15
    '''
    