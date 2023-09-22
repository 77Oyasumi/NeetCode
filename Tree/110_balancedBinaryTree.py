from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balance = (left[0] and right[0] and
            abs(left[1] - right[1]) <= 1)

            return [balance, 1+max(left[1], right[1])]
        return dfs(root)[0]
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            return 1 + max(left, right)

        def check_balance(node):
            if not node:
                return True

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                return False

            return check_balance(node.left) and check_balance(node.right)

        return check_balance(root)
'''

if __name__ == "__main__":
    # 构建第一个二叉树: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    # 构建第二个二叉树: [1,2,2,3,3,null,null,4,4]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)

    solution = Solution()
    
    # 测试第一个二叉树是否为平衡二叉树
    print("Is the first tree balanced?", solution.isBalanced(root1))

    # 测试第二个二叉树是否为平衡二叉树
    print("Is the second tree balanced?", solution.isBalanced(root2))