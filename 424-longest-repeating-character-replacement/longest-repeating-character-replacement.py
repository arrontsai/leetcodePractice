class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        long_len = -float('inf')
        map = collections.defaultdict(int)
        while r < len(s):
            map[s[r]] += 1
            cell_count = r - l + 1
            if cell_count - max(map.values())<=k:
                long_len = max(long_len, cell_count)
            else:
                map[s[l]] -= 1
                l += 1
            r += 1
        return long_len

		