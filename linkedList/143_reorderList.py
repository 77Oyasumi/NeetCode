from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    
    # 先印出原始順序
    original_head = head
    print("Original sequence:")
    while original_head:
        print(f"{original_head.val} -> ", end="")
        original_head = original_head.next
    print("None")
    
    solution = Solution()
    solution.reorderList(head)
    
    # 再印出交錯排列後的結果
    print("Reordered sequence:")
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print("None")