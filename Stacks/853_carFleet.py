from typing import List

class Solution:
    def carfleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(pos, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
solution = Solution()


if __name__ == "__main__":

    target = 12; position = [10,8,0,5,3]; speed = [2,4,1,1,3]
    print(solution.carfleet(target, position, speed))

    target1 = 10; position1 = [3]; speed1 = [3]
    print(solution.carfleet(target1, position1, speed1))

    target2 = 100; position2 = [0,2,4]; speed2 = [4,2,1]
    print(solution.carfleet(target2, position2, speed2))