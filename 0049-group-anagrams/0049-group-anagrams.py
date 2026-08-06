class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            c = ''.join(sorted(s))
            if c in res:
                res[c].append(s)
            else:
                res[c] = [s]
        return list(res.values())
                