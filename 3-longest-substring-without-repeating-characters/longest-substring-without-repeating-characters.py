class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        charSet = set()
        left = 0
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLen = max(maxLen, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLen
