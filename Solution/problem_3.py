# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
import json
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def serialize(root):
    tree_data = {}
    if root == None:
        return
    tree_data['data'] = root.data
    if root.left:
        tree_data['left'] = serialize(root.left)
    if root.right:
        tree_data['right'] = serialize(root.right)
    return json.dumps(tree_data)
def deserialize(s):
    if s == None:
        return
    string = json.loads(s)
    data = string['data']
    left = right = None
    if string.get('left'):
        left = deserialize(string.get('left'))
    if string.get('right'):
        right = deserialize(string.get('right'))
    return Node(data, left, right)    
if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.data == 'left.left'