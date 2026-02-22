class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt1 = 0 
        cnt2 = 0
        for c in s:
            if c == "(":
                cnt1 += 1
                cnt2 += 1
            elif c == ")":
                cnt1 -= 1
                cnt2 -= 1
            else:
                cnt1 -= 1 #* as )
                cnt2 += 1 #* as (
            
            if cnt2 < 0:
                return False
            cnt1 = max(cnt1, 0) #* as str
        return cnt1 == 0

                
            
            