class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while s[l].isalnum() == False and l < r:
                l += 1

            while s[r].isalnum() == False and l < r:
                r -= 1

            if s[l].upper() != s[r].upper():
                return False

            l += 1
            r -= 1

        return True
