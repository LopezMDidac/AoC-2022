
class Folder:
    name: str
    size: int
    subfolders: dict[str, "Folder"]
    parent_folder: "Folder"

    def __init__(self, name, parent_folder = None):
        self.name = name
        self.size = 0
        self.parent_folder=parent_folder
        self.subfolders = dict()
    
    def add_subdir(self, name):
        self.subfolders[name] = Folder(name, self)
    
    def add_size (self, size):
        self.size += size

    def get_subfolder(self, name):
        return self.subfolders[name]

    def process_subfolder_size(self):
        for k,v in self.subfolders.items():
            v.process_subfolder_size()
            self.size += v.size


def calc_total_less(n, root ):
    total = 0
    for k,v in root.subfolders.items():
        total += calc_total_less(n, v)

    if root.size < n:
        total += root.size
        
    return total

def choose_closer_size(target_space, candidate_one, candidate_two):
    candidate_score = candidate_one - target_space
    root_score = candidate_two- target_space

    if candidate_score < 0:
        return candidate_two
    if root_score < 0:
        return candidate_one
    
    if candidate_score < root_score:
        return candidate_one
    else:
        return candidate_two

def find_target_folder(target_space:int, root_folder:Folder):
    candidate = 0
    for k,v in root_folder.subfolders.items():
        candidate_two = find_target_folder(target_space, v)
        candidate = choose_closer_size(target_space, candidate, candidate_two)
    
    return choose_closer_size(target_space, candidate, root_folder.size)
