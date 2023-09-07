from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergelists(l1, l2))
            lists = mergedLists
        return lists[0]
        
        
    def mergelists(self, l1, l2):
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
    # 创建一些测试用例
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(6)))
    list3 = ListNode(2, ListNode(7, ListNode(8)))

    # 创建一个 Solution 实例
    solution = Solution()

    # 合并测试用例
    merged_list = solution.mergeKLists([list1, list2, list3])

    # 打印合并后的链表
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    print(f"None")