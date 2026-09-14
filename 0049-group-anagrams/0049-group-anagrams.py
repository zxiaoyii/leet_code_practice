class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            a = ''.join(sorted(s))
            d[a].append(s)
        return list(d.values())