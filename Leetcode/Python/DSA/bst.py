class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Bst:
    def __init__(self):
        self.root =None
    def create_node(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root=new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")
    def contains(self,value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

my_bst = Bst()
print(my_bst.create_node(1))
print(my_bst.create_node(2))
print(my_bst.create_node(0))
print(my_bst.create_node(10))
print(my_bst.create_node(10))
my_bst.print_tree()
print(my_bst.contains(10))
# print(my_bst.root.value)
# print(my_bst.root.right.value)
# print(my_bst.root.left.value)

