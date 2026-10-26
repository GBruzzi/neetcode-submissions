class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        soma = 0
        path = []
        res = []

        def bt(index):
            nonlocal soma
            if soma == target:
                res.append(path.copy())
                return

            if index == len(candidates) or soma > target:
                return

            path.append(candidates[index])
            soma += candidates[index]
            bt(index)

            path.pop()
            soma -= candidates[index]
            bt(index + 1)

        bt(0)

        return res