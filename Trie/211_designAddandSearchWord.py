class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)

if __name__ == "__main__":
        # 創建一個 WordDictionary 物件
    word_dict = WordDictionary()

    # 添加單詞
    word_dict.addWord("apple")
    word_dict.addWord("banana")
    word_dict.addWord("orange")

    # 進行搜尋
    print(word_dict.search("apple"))    # True
    print(word_dict.search("app"))      # False
    print(word_dict.search("b.n.na"))    # True，因為通配符 '.' 可以匹配任意字符
    print(word_dict.search("xyz"))       # False