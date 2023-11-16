from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(4)

    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(8)

    root.right.left.left = TreeNode(11)
    root.right.left.right = TreeNode(13)

    root.right.right.left = TreeNode(16)
    root.right.right.right = TreeNode(20)

    solution = Solution()

    print(f"{solution.kthSmallest(root, 3)}")
    print(f"{solution.kthSmallest(root, 4)}")
    print(f"{solution.kthSmallest(root, 5)}")
    print(f"{solution.kthSmallest(root, 6)}")
    print(f"{solution.kthSmallest(root, 7)}")
