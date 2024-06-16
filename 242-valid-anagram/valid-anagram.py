class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        map = [0] * 128
        for i in range(len(s)):
            map[ord(s[i])] += 1
            map[ord(t[i])] -= 1
        print(map)
        return True if all(n==0 for n in map) else False
        