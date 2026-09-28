class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        copia = piles.copy()
        res = 0

        while l <= r:
            meio = (l + r) // 2
            
            soma = 0
            for i in range(len(piles)):
                copia[i] = math.ceil(piles[i]/meio)

                soma += copia[i]

            if soma <= h:
                res = meio
                r = meio - 1

            if soma > h:
                l = meio + 1

            else:
                r = meio - 1
            
        return res