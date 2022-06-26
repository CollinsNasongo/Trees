# This class represents a normal tree node (not a binary tree)
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{self.data}"

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


# this function reverses a list
def reverser(lst):
    lst.reverse()
    return lst


# return a list of nodes n with index 0 as the root node and index n as the target node
def get_path(node):
    path = list()
    path.append(node)

    while node.parent:
        path.append(node.parent)
        node = node.parent
        continue

    return reverser(path)


# uses the list from the get_path function to get the level of a node on a tree
def get_level(node):
    lst = get_path(node)
    level = len(lst) - 1
    return level


# displays the structure of a node (visual appeal)
def display(node):
    lvl = "--"

    if len(node.children) != 0:
        print(f"{lvl * get_level(node)} {node.data}")
        for i in node.children:
            display(i)

    else:
        print(f"{lvl * get_level(node)} {node.data}")


# Building a tree for testing

electronics = Node("Electronics")

phones = Node("Phones")
tvs = Node("Televisions")
laptops = Node("Laptops")

samsung = Node("Samsung")
nokia = Node("Nokia")

lg = Node("LG")
hisense = Node("Hisense")

hp = Node("HP")
lenovo = Node("Lenovo")

phones.add_child(samsung)
phones.add_child(nokia)

laptops.add_child(hp)
laptops.add_child(lenovo)

tvs.add_child(lg)
tvs.add_child(hisense)

electronics.add_child(phones)
electronics.add_child(tvs)
electronics.add_child(laptops)


# Uncomment individual lines to test
# display(electronics)
# get_level(lenovo)
# get_path(lenovo)
