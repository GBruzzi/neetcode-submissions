class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for value in nums:
            if value not in d:
                d[value] = 1
            else:
                d[value] += 1

        res = []

        for chave,valor in d.items():
            heapq.heappush(res,(valor,chave))

            if len(res) > k:
                heapq.heappop(res)

        resfinal = []

        for par in res:
            resfinal.append(par[1])

        return resfinal

        


        