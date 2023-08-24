from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
    
if __name__ == "__main__":
    original_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))); n=2

    solution = Solution()

    head = original_head
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print(f"None")
    
    modified_head = solution.removeNthFromEnd(original_head, 2)
    head = modified_head
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print(f"None")