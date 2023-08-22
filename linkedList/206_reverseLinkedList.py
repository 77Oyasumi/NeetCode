from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    current = head

    print(f"Original List: ")
    while current:
        print(f"{current.val} -> ", end="")
        current = current.next
    print(f"None")

    # 創建 Solution 的實例
    solution = Solution()

    # 使用 reverseList 方法進行反轉
    reversed_head = solution.reverseList(head)

    print(f"\nReversed List: ")
    # 輸出反轉後的鏈表值
    while reversed_head:
        print(f"{reversed_head.val} -> ", end="")
        reversed_head = reversed_head.next
    print("None")

'''
Recursive Vision

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
'''