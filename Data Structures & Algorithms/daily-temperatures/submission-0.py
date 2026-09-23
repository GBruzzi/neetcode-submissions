class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []        

        for i in range(n):
            el = temperatures[i]

            
            while stack and el > stack[-1][0] :
                res[stack[-1][1]] = i - stack[-1][1]

                stack.pop()

            stack.append((el, i))


        return res
