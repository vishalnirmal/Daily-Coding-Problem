# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def countUnivalTrees(root):
    if root.left == None and root.right == None:
        return 1
    temp = 0
    if root.left:
        if root.right and root.left.data == root.right.data and root.left.data == root.data:
            temp = 1
        elif root.left.data == root.data:
            temp = 1
    elif root.right:
        if root.left and root.left.data == root.right.data and root.left.data == root.data:
            temp = 1
        elif root.right.data == root.data:
            temp = 1
    return countUnivalTrees(root.left)+countUnivalTrees(root.right)+temp

if __name__ == "__main__":
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    # root = Node(0)
    # root.left = Node(0)
    # root.right = Node(0)
    # root.left.left = Node(1)
    # root.left.right = Node(1)
    # root.left.left.left = Node(1)
    # root.left.left.right = Node(1)
    print(countUnivalTrees(root))
