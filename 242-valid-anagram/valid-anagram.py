class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 用hashmap去算每個字母出現幾次，如過s存完後，t可以把所有的hashmap都削掉就是正確的
        # 特殊狀況，不用檢查直接回傳
        if len(s) != len(t): return False
        hashMapS = {}
        hashMapT = {}
        for i in range(len(s)):
            if s[i] not in hashMapS.keys():
                hashMapS[s[i]] = 1
            else:
                hashMapS[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in hashMapT.keys():
                hashMapT[t[i]] = 1
            else:
                hashMapT[t[i]] += 1
        return hashMapS == hashMapT
        