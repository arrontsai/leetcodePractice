class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 用hashmap去算每個字母出現幾次，如過s存完後，t可以把所有的hashmap都削掉就是正確的
        # 特殊狀況，不用檢查直接回傳
        if len(s) != len(t): return False
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap.keys():
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in hashMap.keys():
                return False
            else:
                hashMap[t[j]] -= 1
        for num in hashMap.values():
            if num != 0:
                return False
        return True