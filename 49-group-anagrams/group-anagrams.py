class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = len(strs)
        # map = [[0]*128 for _ in range(n)]
        # for s in range(n):
        #     for j in strs[s]:
        #         map[s][ord(j)] += 1
        # print(map)
        anagrams = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            print(sorted_str)
            anagrams[sorted_str].append(s)
        return list(anagrams.values())

    