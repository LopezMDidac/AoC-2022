from data import test_data, all_data
from rules import priority_weight

# PART 1
total_prio = 0

for i in all_data:
    first_comp = set(i[:len(i)//2])
    last_comp = set(i[len(i)//2:])
    intersect = first_comp.intersection(last_comp)
    total_prio += sum([priority_weight[el] for el in intersect])


print(total_prio)

# PART 2
total_prio = 0
grouped_data = zip(*(iter(all_data),) * 3)
for i in grouped_data:
    first_oompa = set(i[0])
    second_oompa = set(i[1])
    third_oompa = set(i[2])
    badge = first_oompa.intersection(second_oompa).intersection(third_oompa).pop()
    total_prio += priority_weight[badge]

print(total_prio)