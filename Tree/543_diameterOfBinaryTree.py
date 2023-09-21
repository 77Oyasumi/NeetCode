from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0] # recording max diameter

        def dfs(root): # find the height
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right) # 2 => 1 左子樹的height + 1 右子樹的height

            return 1 + max(left, right)
        dfs(root)
        return res[0]

if __name__ == "__main__":
    # 測試資料1
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)
    solution = Solution()
    result1 = solution.diameterOfBinaryTree(tree1)
    print("Test 1 - Expected: 3, Actual:", result1)

    # 測試資料2
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    solution = Solution()
    result2 = solution.diameterOfBinaryTree(tree2)
    print("Test 2 - Expected: 1, Actual:", result2)

