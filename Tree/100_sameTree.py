from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
if __name__ == "__main__":
    # Test case 1: Both trees are empty, should return True
    solution = Solution()
    result1 = solution.isSameTree(None, None)
    print("Test case 1:", result1)  # Expected output: True

    # Test case 2: One tree is empty, should return False
    result2 = solution.isSameTree(TreeNode(1), None)
    print("Test case 2:", result2)  # Expected output: False

    # Test case 3: Trees are different, should return False
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(4))
    result3 = solution.isSameTree(tree1, tree2)
    print("Test case 3:", result3)  # Expected output: False

    # Test case 4: 
    tree3 = TreeNode(1, TreeNode(3), TreeNode(2))
    tree4 = TreeNode(1, TreeNode(2), TreeNode(3))
    result4 = solution.isSameTree(tree3, tree4)
    print("Test case 4:", result4)
