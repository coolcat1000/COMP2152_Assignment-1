"""
Author: Jessica Wisnoski
Assignment: #1

"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"  # string
preferred_weight_kg = 20.5  # float
highest_reps = 25           # int
membership_active = True    # bool


# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (30, 45, 20),  # (yoga, running, lifting)
    "Jamie": (25, 42, 30),
    "Taylor": (21, 35, 22)
}

# Step d: Calculate total workout minutes (store separately — cleaner & safer)
names = list(workout_stats.keys())

for name in names:
    total_minutes = sum(workout_stats[name])
    workout_stats[f"{name}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
workout_list = [list(workout_stats[name]) for name in names]

# Step f: Slice the workout_list
print("\nYoga and Running minutes for all friends:")
for friend_minutes in workout_list:
    print(friend_minutes[:2])  # yoga + running

print("\nWeightlifting minutes for the last two friends:")
for friend_minutes in workout_list[-2:]:
    print(friend_minutes[2])   # weightlifting


# Step g: Check if any friend's total >= 120
print("\nActivity recognition:")
for name in names:
    if workout_stats[f"{name}_Total"] >= 120:
        print(f"Great job staying active, {name}!")

# Step h: User input to look up a friend (case-insensitive friendly)
query = input("\nEnter a friend's name: ").strip().title()

if query in workout_stats and not query.endswith("_Total"):
    stats = workout_stats[query]
    print(f"\n{query}'s workout minutes:")
    print(f"Yoga: {stats[0]}")
    print(f"Running: {stats[1]}")
    print(f"Weightlifting: {stats[2]}")
    print(f"Total: {workout_stats[f'{query}_Total']} minutes")
else:
    print(f"\nFriend {query} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes
totals_only = {name: workout_stats[f"{name}_Total"] for name in names}

max_friend = max(totals_only, key=totals_only.get)
min_friend = min(totals_only, key=totals_only.get)

print("\nWorkout Summary:")
print(f"Highest total workout minutes: {max_friend} ({totals_only[max_friend]} minutes)")
print(f"Lowest total workout minutes: {min_friend} ({totals_only[min_friend]} minutes)")
