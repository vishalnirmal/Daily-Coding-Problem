# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.isLocked = False
        self.parentLocked = False
    
    def is_locked(self):
        return self.isLocked

    def set_parent_lock(self, bool):
        if self.left:
            self.left.set_parent_lock(bool)
        if self.right:
            self.right.set_parent_lock(bool)
        self.parentLocked = bool

    def locked_descedants(self):
        if self.right:
            if self.right.isLocked:
                return True
            else:                
                return self.locked_descedants(self.right)
        if self.left:
            if self.left.isLocked:
                return True
            else:           
                self.locked_descedants(self.left)     
                return self.locked_descedants(self.left)
        return False

    def lock(self):
        if self.parentLocked and self.locked_descedants():
            return False
        else:
            self.isLocked = True
            self.set_parent_lock(True)
            self.parentLocked = False
            return True

    def unlock(self):
        if self.parentLocked and self.locked_descedants():
            return False
        else:
            self.isLocked = False
            self.set_parent_lock(False)
            return True            

if __name__ == "__main__":
    node = Node(4, Node(5, Node(7, Node(8), Node(9)), Node(10, Node(11), Node(12))), Node(6, Node(13, Node(14), Node(15)), Node(16, Node(17), Node(18))))
    print(node.left.lock())
    print(node.right.left.lock())
    print(node.left.unlock())
    print(node.right.left.unlock())
    
    
