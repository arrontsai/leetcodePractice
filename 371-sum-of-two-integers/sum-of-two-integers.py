class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0b11111111111111111111111111111111
        while b & mask != 0:
            carry = (a & b)<< 1
            a = a ^ b
            b = carry
        if b > mask:
            return a & mask
        else:
            return a