class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t = Counter(s1)
        l = 0
        window = defaultdict(int)
        for r, c in enumerate(s2):
            window[c] += 1
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            if window == t:
                return True
            
        return False

            
