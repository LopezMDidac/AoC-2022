from data import test_data, all_data

calories = all_data
elves_cal = list()

partial_cal = 0
for cal in calories:
    if cal == "":
        elves_cal.append(partial_cal)
        partial_cal = 0
    else:
        partial_cal += cal

elves_cal.append(partial_cal)
sorted_elves = sorted(elves_cal,reverse=True)

## PART 1
print(sorted_elves[0])

## PART 2
print(sorted_elves[0] + sorted_elves[1] + sorted_elves[2])



max_cal = max(elves_cal)
sorted_elves = sorted(elves_cal,reverse=True)
print( sorted_elves)
max_cal = sorted_elves[0] + sorted_elves[1] + sorted_elves[2] 
print(max_cal)
