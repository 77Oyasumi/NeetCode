from typing import List

class Solution:
    def dailyTemp(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = [] # pair

        for i, t in enumerate(temps):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
    
if __name__ == "__main__":
    solution = Solution()
    
    temperatures1 = [73,74,75,71,69,72,76,73]
    print(solution.dailyTemp(temperatures1)) # [1,1,4,2,1,1,0,0]

    temperatures2 = [30,40,50,60]
    print(solution.dailyTemp(temperatures2)) # [1,1,1,0]

    temperatures3 = [30,60,90]
    print(solution.dailyTemp(temperatures3)) # [1,1,0]