class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            meio = (l + r) // 2
            
            soma = 0
            for i in range(len(piles)):
                soma += math.ceil(piles[i]/meio)

            if soma <= h:
                res = meio
                r = meio - 1

            elif soma > h:
                l = meio + 1
            
        return res