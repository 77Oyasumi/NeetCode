from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
    
if __name__ == "__main__":
    # 建立 list1 和 list2
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    # 顯示 list1 原本的樣子
    print("List 1 original:")
    current = list1
    while current:
        print(f"{current.val} -> ", end="")
        current = current.next
    print("None\n")

    # 顯示 list2 原本的樣子
    print("List 2 original:")
    current = list2
    while current:
        print(f"{current.val} -> ", end="")
        current = current.next
    print("None\n")

    # 建立 Solution 物件
    solution = Solution()

    # 合併 list1 和 list2
    merged_list = solution.mergeTwoLists(list1, list2)

    # 顯示合併後的結果
    print("Merged list:")
    current = merged_list
    while current:
        print(f"{current.val} -> ", end="")
        current = current.next
    print("None\n")
