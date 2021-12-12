#!/usr/bin/env python3

# constants
NEW_FISH = 8
FISH_RESET = 6
FISH_READY = 0
DAYS_PART_ONE = 80
DAYS_PART_TWO = 256

f = open('input', 'r')

# list of all fish
fish = list(map(int, f.readline().rstrip().split(",")))

# this list is the number of fish with (index) days left.
# it's always NEW_FISH + 1 long after initialization
days = []
for index in range(NEW_FISH + 1):
    count = 0
    # count all fish that have (index) days left
    for one_fish in fish:
        if one_fish == index:
            count += 1
    days.append(count)
# days [] is now initialized

# this is fast because it's O(DAYS)
for day in range(DAYS_PART_TWO):
    # remember ready fish
    ready_fish = days[FISH_READY]
    # decrease all non ready fish
    # this is O(NEW_FISH), i.e. constant
    for i in range(FISH_READY + 1, NEW_FISH +1):
        days[i-1] = days[i]
    # create new fish
    days[NEW_FISH] = ready_fish
    # reset ready fish
    days[FISH_RESET] += ready_fish
    if day == DAYS_PART_ONE - 1:
        # count fish after DAYS_PART_ONE days
        count = 0
        for num in days:
            count += num
        print("After", DAYS_PART_ONE, "days, there are", count, "fish")

# count fish after DAYS_PART_TWO days
count = 0
for num in days:
    count += num
print("After", DAYS_PART_TWO, "days, there are", count, "fish")

# this takes way too long because it's O(len(fish)), i.e. O(n^2)
# for day in range(DAYS_PART_TWO):
#     print("day", day)
#     i = len(fish) - 1
#     while i >= 0:
#         if fish[i] == FISH_READY:
#             fish.append(NEW_FISH)
#             fish[i] = FISH_RESET
#         else:
#             fish[i] -= 1
#         i -= 1
#     if day == DAYS_PART_ONE - 1:
#         print("Part1: After", DAYS_PART_ONE, "days, there will be", len(fish), "lanternfish.")
# print("Part2: After", DAYS_PART_TWO, "days, there will be", len(fish), "lanternfish.")
