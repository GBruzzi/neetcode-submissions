class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        end = len (matrix) - 1

        while start <= end:
            meio = (start + end) // 2

            el = matrix[meio][0]

            if target >= matrix[meio][0] and target <= matrix[meio][-1]:
                l = 0
                r = len(matrix[meio]) - 1
               
                while l <= r:
                    meio2 = (r + l) // 2

                    el = matrix[meio][meio2]
                    if target == el:
                        return True
                    elif el > target:
                        r = meio2 - 1
                    else:
                        l = meio2 + 1

                return False  

            elif target < matrix[meio][0]:
                end = meio - 1
            else:
                start = meio + 1

        return False