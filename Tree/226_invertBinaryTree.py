from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
if __name__ == "__main__":
    # Create a binary tree using the given representation [4,2,7,1,3,6,9]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # Print the original tree
    print("Original Tree:")
    print("     4 ")
    print("    / \\")
    print("   2   7 ")
    print("  / \\ / \\")
    print(" 1  3 6  9")

    # Invert the tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    # Print the inverted tree
    print("\nInverted Tree:")
    print("     4 ")
    print("    / \\")
    print(f"   {inverted_root.left.val}   {inverted_root.right.val}")
    print("  / \\ / \\")
    print(f" {inverted_root.left.left.val}  {inverted_root.left.right.val} {inverted_root.right.left.val} {inverted_root.right.right.val}")