class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to value

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev # double linked list

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    # 创建一个容量为 2 的 LRUCache
    cache = LRUCache(2)

    # 添加一些键值对到缓存中
    cache.put(1, 1)
    cache.put(2, 2)

    # 获取键 1 的值，应该返回 1
    print(cache.get(1))

    # 添加一个新键值对，会使得键 2 成为 LRU，因为容量为 2
    cache.put(3, 3)

    # 获取键 2 的值，应该返回 -1，因为它已经被淘汰出缓存
    print(cache.get(2))

    # 添加一个新键值对，会使得键 1 成为 LRU
    cache.put(4, 4)

    # 获取键 1 的值，应该返回 -1，因为它已经被淘汰出缓存
    print(cache.get(1))

    # 获取键 3 的值，应该返回 3
    print(cache.get(3))

    # 获取键 4 的值，应该返回 4
    print(cache.get(4))

