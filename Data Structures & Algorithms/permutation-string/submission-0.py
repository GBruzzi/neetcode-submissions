class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}

        for c in s1:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        l,r = 0,0

        while r < len(s2):
            if s2[r] in d and d[s2[r]] > 0:
                d[s2[r]] -= 1

                if (r - l + 1) == len(s1):
                    return True
            else:
                if l == r:
                    l += 1
                    r += 1
                    continue

                while s2[l] != s2[r]:
                    d[s2[l]] += 1
                    l += 1
            
                l += 1

            r += 1

        return False

        
