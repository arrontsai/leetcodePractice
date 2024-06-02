class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        string_b  = bin(n)[2:]
        for i in string_b:
            if i =='1':
                count += 1
        return count