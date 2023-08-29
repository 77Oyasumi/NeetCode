from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hashCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
            
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
                
        return False
    
    def floydCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
    
if __name__ == "__main__":

    solution = Solution()

    # 測試用例 1: 存在循環
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 循環點

    print(solution.hashCycle(node1))  # 應該輸出 True
    print(solution.floydCycle(node1))

    # 測試用例 2: 不存在循環
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(solution.hashCycle(node1))  # 應該輸出 False
    print(solution.floydCycle(node1))

    # 測試用例 3: 存在循環
    node1 = ListNode(1)
    node2 = ListNode(2)

    node1.next = node2
    node2.next = node1  # 循環點

    print(solution.hashCycle(node1))  # 應該輸出 True
    print(solution.floydCycle(node1))  # 應該輸出 True

    node1 = ListNode(1)

    print(solution.hashCycle(node1))  # 應該輸出 True
    print(solution.floydCycle(node1))  # 應該輸出 True