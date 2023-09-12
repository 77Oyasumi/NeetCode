from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

if __name__ == "__main__":
    # 創建一個測試用的單向鏈表，例如：1 -> 2 -> 3 -> 4 -> 5
    test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # 創建 Solution 實例
    solution = Solution()

    # 測試反轉 k 個節點，例如 k = 2
    k = 2
    result = solution.reverseKGroup(test_list, k)

    # 打印反轉後的結果，應該是：2 -> 1 -> 4 -> 3 -> 5
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
