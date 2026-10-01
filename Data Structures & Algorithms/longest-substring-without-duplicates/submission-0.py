class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 1
        l,r = 0,0

        seen = set()
        seen.add(s[0])

        while r < len(s) - 1:
            r += 1
            
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
                seen.add(s[r])
            else:
                seen.add(s[r])

                res = max(res, r + 1 - l)

        return res