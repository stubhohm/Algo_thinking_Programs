'''
Involves the construction and assement of a family tree via nodes and graph traversal.
'''

MAX_NAMES = 10

class FamilyMember():
    def __init__(self, name, number_of_children):
        self.name = name
        self.numbuer_of_children = number_of_children
        self.children = []


def new_child(name):
    new_node = FamilyMember(name, 0)
    return new_node

def new_parent(name, number_of_children):
    new_node = FamilyMember(name, number_of_children)
    return new_node

def find_nodes(name, current_tree):
    for node in current_tree:
        if node.name == name:
            return node
    else:
        return None

def parse_input(data):
    split_data = data.split()
    parent_name = split_data[0]
    parent_num_of_children = int(split_data[1])
    children_names = split_data[2:]
    return parent_name, parent_num_of_children, children_names

def add_member(current_tree):
    input_data = input('Enter a Parents name, the number of children they have, and their childrens names:')
    if input_data == 'Done':
        return False
    parent_name, parent_num_of_children, children_names = parse_input(input_data)
    parent = find_nodes(parent_name, current_tree)
    if not parent:
        parent = new_parent(parent_name, parent_num_of_children)
        current_tree.append(parent)
    for children in children_names:
        child = find_nodes(children, current_tree)
        if not child:
            print(f'Did not fild {children}')
            child = new_child(children)
            current_tree.append(child)
        else:
            print(f'Found {children} via {child} with name {child.name}')
        parent.children.append(child)
    return True

def find_descendants(node):
    descendants = 0
    if len(node.children) == 0:
        return 1
    for child in node.children:
        children = find_descendants(child)
        descendants = descendants + children
    return descendants

def find_root(current_tree):
    max_descendants = 0
    for node in current_tree:
        descendants = find_descendants(node)
        if descendants > max_descendants:
            max_descendants = descendants
            current_root = node
    return current_root
    
def print_tree(root):
    if len(root.children) == 0:
        print(f'{root.name} has no children')
        return
    print(f'{root.name} has {len(root.children)} children.')
    for child in root.children:
        print(f'They are {child.name}.')
    for child in root.children:
        print_tree(child)
    return

def print_family_tree(current_tree):
    root = find_root(current_tree)
    print_tree(root)
    



def main():
    current_tree = []
    while len(current_tree) < MAX_NAMES:
        if not add_member(current_tree):
            break
    print_family_tree(current_tree)

main()