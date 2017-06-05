# you'll implement search() and insert() for binary search tree.
# You should rewrite search() and not use your code from the last exercise so it takes advantage of BST properties

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        pass

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                return self.preorder_search(start.left, find_val)
            else:
                return self.preorder_search(start.right, find_val)
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
