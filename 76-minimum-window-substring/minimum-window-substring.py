class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        map = collections.defaultdict(int)
        start, end = 0, 0
        count = len(t)
        min_len = float('inf')
        start_index = 0
        for c in t:
            map[c] += 1
        print(map)
        while end < len(s):
            # 更新end
            if map[s[end]]>0:
                count -= 1
            map[s[end]] -= 1
            end += 1
            while count == 0:
                #更新min_len
                if end - start < min_len:
                    min_len = end - start
                    start_index = start
                #更新start
                if map[s[start]] == 0:
                    count += 1
                map[s[start]] += 1
                start += 1
                
        return s[start_index:start_index + min_len] if min_len != float('inf') else ""
            
