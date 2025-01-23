from typing import List

# bucket sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq= [[] for i in range(len(nums) + 1)] #如果不+1 下面temp[c]時 你會少一個可能 就是整串數列都是同一個數字的那個數目 好比3個3 你的temp就只有[0],[1],[2]而少了[3]


        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): # 反轉術式 bucket sort
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            if len(res) < k:
                res.extend(freq[i])

        return res

#        for i in range(len(freq) - 1, 0, -1): #為什麼又要-1? 就拿上面3個3的例子 你這樣會有4個[], [0],[1],[2],[3] 所以你len(temp)會是4 但問題是你沒有temp[4]啊 這樣就會index out of range)
#            for n in freq[i]:
#                res.append(n)
#                if len(res) == k:
#                    return res

# extend v.s append

# extend會把裡面的元素抓出來放進去, append就是那東東長怎樣 就整包給你包進去
# 用這個例子來說 temp[6]會是空的 因為沒有出現6個的數字嘛 temp[5] temp[4]同理 所以你用append 就會直接把[6]跟[5]的[]給你丟到res裡面了
# 所以你res就變成[[], []] 然後長度剛好是2 就停止了
# 用extend就會因為temp[6] [5] [4]內沒元素 就不放 到了[3]才把[3]內的元素放進去(2個)
                
# from typing import List
# from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = defaultdict(int)
#         freq = [[] for i in range(len(nums) + 1)]

#         for n in nums:
#             count[n] += 1

#         for n, c in count.items():
#             freq[c].append(n)

#         res = []

#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res

solution = Solution()

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10]
k = 3

result = solution.topKFrequent(nums, k)
print(result)
                
solution = Solution()

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10]
k = 3

result = solution.topKFrequent(nums, k)
print(result)
