# Movie Rating System

# Step 1: Input ratings
ratings = []
n = int(input("Enter number of ratings: "))

for i in range(n):
    r = int(input(f"Enter rating {i+1} (1–5): "))
    ratings.append(r)

print("\nOriginal Ratings:", ratings)

# Step 2: Remove invalid ratings (not between 1 and 5)
valid_ratings = []

for r in ratings:
    if 1 <= r <= 5:
        valid_ratings.append(r)

if len(valid_ratings) == 0:
    print("No valid ratings available.")
else:
    print("Valid Ratings:", valid_ratings)

    # Step 3: Find average rating
    average = sum(valid_ratings) / len(valid_ratings)
    print("Average Rating:", average)

    # Step 4: Count 5-star ratings
    five_star_count = valid_ratings.count(5)
    print("Number of 5-Star Ratings:", five_star_count)

    # Step 5: Sort ratings in ascending order
    valid_ratings.sort()
    print("Sorted Ratings (Ascending):", valid_ratings)

    '''output:
    Enter number of ratings: 7
    Enter rating 1 (1–5): 5
    Enter rating 2 (1–5): 4
    Enter rating 3 (1–5): 3
    Enter rating 4 (1–5): 6
    Enter rating 5 (1–5): 2
    Enter rating 6 (1–5): 0
    Enter rating 7 (1–5): 5
    Original Ratings: [5, 4, 3, 6, 2, 0, 5]
    Valid Ratings: [5, 4, 3, 2, 5]
    Average Rating: 3.8
    Number of 5-Star Ratings: 2

    Sorted Ratings (Ascending): [2, 3, 4, 5, 5]
    '''
    