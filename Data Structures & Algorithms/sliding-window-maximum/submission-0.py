from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        l,r = 0,k - 1
        res = []
        n = len(nums)

        for i in range(r + 1) :
            while len(dq) and nums[i] > nums[dq[-1]]:
                dq.pop()

            dq.append(i)


        res.append(nums[dq[0]])

        while r < n - 1:
            r += 1
            l += 1

            exp = r - k + 1

            if dq[0] < exp:
                dq.popleft()
            
            while len(dq) and nums[r] > nums[dq[-1]]:
                dq.pop()

            dq.append(r)

            res.append(nums[dq[0]])

        return res