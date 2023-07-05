from collections import defaultdict
from typing import List

class Solution:
    def groupAnagram(self, strs:list[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
#       result = [(i, value) for i, (_, value) in enumerate(res.items())]
        return  res.values()
#       return  result   # index同時與values印出來 就[(0, ['eat', 'tea', 'ate']), (1, ['tan', 'nat']), (2, ['bat'])]
    
# 測試用例1：包含多組相同字母組成的單詞
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 預期輸出：dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(Solution().groupAnagram(strs1))

# 測試用例2：只有單詞本身
strs2 = ["hello", "world", "python"]
# 預期輸出：dict_values[['hello'], ['world'], ['python']]
print(Solution().groupAnagram(strs2))

# 測試用例3：空列表
strs3 = []
# 預期輸出：dict_values[]
print(Solution().groupAnagram(strs3))