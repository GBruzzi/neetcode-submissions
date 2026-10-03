class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        res = 0
        d = {}

        while r < len(s) :
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1

            exp = (r - l + 1) - max(d.values())

            while exp > k:
                d[s[l]] -= 1
                l += 1
                exp -= 1

            res = max(res,r - l + 1)  
            r += 1        

        return res
        
