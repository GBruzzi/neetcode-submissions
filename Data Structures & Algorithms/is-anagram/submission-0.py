class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dictA = {}
        dictB = {}

        for char in s:
            if char in dictA:
                dictA[char] += 1
            else :
                dictA[char] = 1

        for char in t:
            if char in dictB:
                dictB[char] += 1
            else :
                dictB[char] = 1

        for key in dictA:
            if key in dictB:
                if dictA[key] != dictB[key]:
                    return False
            else:
                return False


        return True