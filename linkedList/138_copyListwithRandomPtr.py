from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDict = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copyDict[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copyDict[curr]
            copy.next = copyDict[curr.next]
            copy.random = copyDict[curr.random]
            curr = curr.next
        
        return copyDict[head]
    
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1
    copied_node1 = solution.copyRandomList(node1)
    cur = copied_node1
    while cur:
        print(f"Node val: {cur.val}, Next val: {cur.next.val if cur.next else None}, Random val: {cur.random.val if cur.random else None}")
        cur = cur.next
    print("\n")

    # Test Case 2
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node1.random = node2
    node2.random = node2
    copied_node1 = solution.copyRandomList(node1)
    cur = copied_node1
    while cur:
        print(f"Node val: {cur.val}, Next val: {cur.next.val if cur.next else None}, Random val: {cur.random.val if cur.random else None}")
        cur = cur.next
    print("\n")

    # Test Case 3
    node1 = Node(3)
    node2 = Node(3)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    copied_node1 = solution.copyRandomList(node1)
    cur = copied_node1
    while cur:
        print(f"Node val: {cur.val}, Next val: {cur.next.val if cur.next else None}, Random val: {cur.random.val if cur.random else None}")
        cur = cur.next