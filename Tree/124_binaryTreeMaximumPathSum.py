from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
    
if __name__ == "__main__":
    #          -9
    #         /  \
    #       -2    7
    #       / \  / \
    #      8  -4 2  -1
    tree_root = TreeNode(-9)
    tree_root.left = TreeNode(-2)
    tree_root.right = TreeNode(7)
    tree_root.left.left = TreeNode(8)
    tree_root.left.right = TreeNode(-4)
    tree_root.right.left = TreeNode(2)
    tree_root.right.right = TreeNode(-1)

    # 创建 Solution 实例
    sol = Solution()

    # 调用 maxPathSum 方法并打印结果
    result = sol.maxPathSum(tree_root)
    print("Maximum Path Sum:", result)