class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1dict, s2dict = {}, {}

        for i in range(len(s1)):
            s1dict[s1[i]] = 1 + s1dict.get(s1[i], 0)
            s2dict[s2[i]] = 1 + s2dict.get(s2[i], 0)

        l = 0

        for r in range(len(s1), len(s2)):
            if s1dict == s2dict:
                return True

            s2dict[s2[r]] = 1 + s2dict.get(s2[r], 0)
            s2dict[s2[l]] -= 1

            if s2dict[s2[l]] == 0:
                del s2dict[s2[l]]
            l += 1
        return s1dict == s2dict
    
if __name__ == "__main__":
    solution = Solution()

    s1 = "ab"; s2 = "eidbaooo"
    print(f"{solution.checkInclusion(s1, s2)}")
    s1 = "ab"; s2 = "eidboaoo"
    print(f"{solution.checkInclusion(s1, s2)}")
    s1 = "adc"; s2 = "dcda"
    print(f"{solution.checkInclusion(s1, s2)}")