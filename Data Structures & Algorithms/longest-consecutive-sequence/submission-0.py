class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        resGlobal = 0

        meuSet = set()
        for n in nums:
            meuSet.add(n)


        for n in meuSet:
            resLocal = 1
            if n-1 not in meuSet:
                while True:
                    if n+1 in meuSet:
                        resLocal += 1
                        
                        n += 1
                    else:
                        break
            if resLocal > resGlobal:
                            resGlobal = resLocal

        
        return resGlobal