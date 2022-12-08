
from data import test_data, all_data


def calculate_zone(limits:str) -> set[int]:
    min_max_zone = [int(limit) for limit in limits.split("-")]
    zone = set(range(min_max_zone[0], min_max_zone[1]+1))
    return zone

## PART 1
overlapped_zones = 0
for i in all_data:
    first_zone = calculate_zone(i[0])
    last_zone = calculate_zone(i[1])
    if first_zone.issubset(last_zone) or first_zone.issuperset(last_zone):
        overlapped_zones +=1

print(overlapped_zones)

## PART 2
overlapped_zones = 0
for i in all_data:
    first_zone = calculate_zone(i[0])
    last_zone = calculate_zone(i[1])
    if not first_zone.isdisjoint(last_zone):
        overlapped_zones +=1

print(overlapped_zones)