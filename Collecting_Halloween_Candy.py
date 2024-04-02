import time
class parent_node():
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


class child_node():
    def __init__(self, name, candy, left, right):
        self.name = name
        self.candy = candy
        self.left = left
        self.right = right

four = child_node('four', 4, None, None)
nine = child_node('nine', 9, None, None)
b = child_node('b', None, four, nine)
fifteen = child_node('fifteen', 15, None, None)
c = child_node('c', None, b, fifteen)
two = child_node('two', 2, None, None)
d = child_node('d', None, c, two)
six = child_node('six', 6, None, None)
three = child_node('three', 3, None, None)
seventy_two = child_node('seventy two', 72, None, None)
a = child_node('a', None, seventy_two, three)
e = child_node('e', None, six, d)
seven = child_node('seven', 7, None, None)
fourty_one = child_node('fourty one', 41, None, None)
g = child_node('g', None, seven, fourty_one)
f = child_node('f', None, a, e)
h = parent_node('h', f, g)

unexplored_path = []

def choose_node_candy(parent_node):
    print(f"parent node {parent_node.name}")
    if isinstance(parent_node.candy, int):
        print(f'Node {parent_node.name} has {parent_node.candy} pieces of candy')
        return parent_node.candy
    print(f'node {parent_node.name} has branches {parent_node.left.name} and {parent_node.right.name}')
    left_branch_candy = choose_node_candy(parent_node.left)
    right_branch_candy = choose_node_candy(parent_node.right)
    total_candy = left_branch_candy + right_branch_candy
    return total_candy

def choose_node_steps(parent_node):
    if isinstance(parent_node.candy, int):
        print(f'Node {parent_node.name} is a house')
        return 0
    print(f'node {parent_node.name} has branches {parent_node.left.name} and {parent_node.right.name}')
    left_branch_steps = choose_node_steps(parent_node.left)
    right_branch_steps = choose_node_steps(parent_node.right)
    branch_steps = left_branch_steps + right_branch_steps + 4
    print(branch_steps)
    return branch_steps

def choose_node_depth(parent_node, depth=0):
    depth = depth + 1
    if isinstance(parent_node.candy, int):
        return depth
    left_branch_depth = choose_node_depth(parent_node.left, depth)
    right_branch_depth = choose_node_depth(parent_node.right, depth)
    if left_branch_depth > right_branch_depth:
        deepest_branch = left_branch_depth
    else:
        deepest_branch = right_branch_depth
    return deepest_branch

def open_tree(parent_node):
    # Total candy on the tree
    left_branch_candy = choose_node_candy(parent_node.left)
    right_branch_candy = choose_node_candy(parent_node.right)
    total_candy = left_branch_candy + right_branch_candy
    print(total_candy)
    
    # Total steps when returning to root
    left_branch_steps = choose_node_steps(parent_node.left)
    right_branch_steps = choose_node_steps(parent_node.right)
    total_steps = left_branch_steps + right_branch_steps + 4
    print(total_steps)

    # Deepest path on the tree
    left_branch_depth = choose_node_depth(parent_node.left)
    right_branch_depth = choose_node_depth(parent_node.right)
    if left_branch_depth > right_branch_depth:
        deepest_branch = left_branch_depth
    else:
        deepest_branch = right_branch_depth
    print(f'Minimun total streets is {total_steps - deepest_branch}')

def construct_tree(string_tree):
    string_tree= string_tree.strip()
    # if it starts and ends with a ( )
    starts_with_paren = string_tree.startswith('(')
    end_with_paren = string_tree.endswith(')')
    if starts_with_paren and end_with_paren:
        # strip off the () and send it back in
        string_tree = string_tree[1:-1]
        left, right = construct_tree(string_tree)
        return left, right
    # if it starts with ( but ends in something else the value is a house the rest is the rest of the tree
    elif starts_with_paren:
        last_paren_index = string_tree.rfind(")")
        if last_paren_index != -1:
            # Extract the substring from the last ")" to the end
            value_str = string_tree[last_paren_index + 1:]
            # Convert the substring to an integer
            try:
                string_tree = string_tree[:last_paren_index + 1]
                value = int(value_str)
                print(f'node value {value}')
                leaf = child_node(value_str, value, None, None)
                l, r = construct_tree(string_tree)
                branch = child_node('branch', None, l, r)
                return leaf, branch
            except ValueError:
                print("Error: Invalid integer value")
                return None, None
    # If it does not start with and does not end with a parenthesis, we are at the root
    else:
        print(f'{string_tree} ends with neither')
        values = string_tree.split()
        left = child_node(f'{values[0]}', int(values[0]), None, None)
        right = child_node(f'{values[1]}', int(values[1]), None, None)
        print(left.name, right.name)
        return left, right
    
def read_tree():
    string_tree = input('Input a Binary Tree String:')
    left, right = construct_tree(string_tree)
    root = parent_node('Root', left, right)
    return root

def main():
    root = read_tree()
    open_tree(root)
    
main()