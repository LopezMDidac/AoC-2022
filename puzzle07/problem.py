from data import test_data, all_data
from rules import Folder, calc_total_less, find_target_folder


current_folder = None
parent_folder = None
for line in all_data:
    if line.startswith("$ cd"):
        name = line.split(" ")[2]
        if current_folder is None:
            current_folder = Folder(name)
            parent_folder = current_folder
        elif name == "..":
            current_folder = current_folder.parent_folder
        else:
            current_folder = current_folder.get_subfolder(name)
        
    elif line == "$ ls":
        pass
    elif line.startswith("dir"):
        name = line.split(" ")[1]
        current_folder.add_subdir(name)
    else:
        size = int(line.split(" ")[0])
        current_folder.add_size(size)

parent_folder.process_subfolder_size()

## PART 1
sum_less_100 = calc_total_less(100000, parent_folder)
print(sum_less_100)

## PART 2
unused_space = 70000000 - parent_folder.size
space_to_free = 30000000 - unused_space

folder_size = find_target_folder(space_to_free, parent_folder)
print(folder_size)