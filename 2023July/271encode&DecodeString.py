class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res

solution = Solution()
input_data = ["apple", "banana", "cherry"]
encoded_string = solution.encode(input_data)
print(encoded_string)
# 輸出：5#apple6#banana6#cherry

decoded_list = solution.decode(encoded_string)
print(decoded_list)
# 輸出：['apple', 'banana', 'cherry']

solution = Solution()
input_data = ["Hello", "world", "!"]
encoded_string = solution.encode(input_data)
print(encoded_string)
# 輸出：5#Hello5#world1#!

decoded_list = solution.decode(encoded_string)
print(decoded_list)
# 輸出：['Hello', 'world', '!']

solution = Solution()
input_data = ["123", "45", "6789"]
encoded_string = solution.encode(input_data)
print(encoded_string)
# 輸出：3#1232#454#6789

decoded_list = solution.decode(encoded_string)
print(decoded_list)
# 輸出：['123', '45', '6789']