class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def StartWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

if __name__ == "__main__":
    # 創建一個 Trie
    trie = Trie()

    # 插入單詞
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    # 搜尋單詞
    print(trie.search("apple"))  # 應該輸出 True
    print(trie.search("app"))    # 應該輸出 True
    print(trie.search("orange")) # 應該輸出 False

    # 搜尋前綴
    print(trie.StartWith("app"))     # 應該輸出 True
    print(trie.StartWith("ban"))     # 應該輸出 True
    print(trie.StartWith("grape"))   # 應該輸出 False
