# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
    
if __name__ == "__main__":
    # 創建一個二叉樹
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # 實例化 Codec
    codec = Codec()

    # 進行序列化
    serialized_tree = codec.serialize(root)
    print("Serialized Tree:", serialized_tree)

    # 進行反序列化
    deserialized_root = codec.deserialize(serialized_tree)

    # 驗證反序列化的結果是否正確
    def validate(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val) and validate(node1.left, node2.left) and validate(node1.right, node2.right)

    is_valid = validate(root, deserialized_root)
    print("Deserialization is valid:", is_valid)