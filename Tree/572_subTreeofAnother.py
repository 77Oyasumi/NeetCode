from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (not root or not subRoot) or (root.val != subRoot.val):
            return False
        return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
    
if __name__ == "__main__":
    main_root = TreeNode(3)
    main_root.left = TreeNode(4)
    main_root.right = TreeNode(5)
    main_root.left.left = TreeNode(1)
    main_root.left.right = TreeNode(2)

    sub_root = TreeNode(4)
    sub_root.left = TreeNode(1)
    sub_root.right = TreeNode(2)

    solution = Solution()
    print(solution.isSubtree(main_root, sub_root))  # 應該印出 True