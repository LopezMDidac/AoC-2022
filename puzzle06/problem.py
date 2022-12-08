from data import test_data, all_data

data = all_data

def calculate_package_position(frame):
    q = list()
    q = [d for d in data[:frame]]

    i = frame
    while len(set(q)) < frame:
        q.append(data[i])
        q.pop(0)
        i += 1
    return i

## PART 1
print(calculate_package_position(4))
## Part 2
print(calculate_package_position(14))