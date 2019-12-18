# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

def length(head):
    temp = head
    count = 0
    while temp != None:
        count += 1
        temp = temp.next
    return count

def findIntersectingNode(head1, head2):
    len1 = length(head1)
    len2 = length(head2)
    diff = abs(len1 - len2)
    temp1, temp2 = (head1, head2) if (len1 > len2) else (head2, head1)
    while diff:
        temp1 = temp1.next
        diff-=1
    while temp1 != None and temp2 != None:
        if temp1.data == temp2.data:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next
    return None


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

if __name__ == "__main__":
    
    node1 = Node(3, Node(7, Node(8, Node(10))))
    node2 = Node(99, Node(1, Node(8, Node(10))))
    print(findIntersectingNode(node1, node2).data)