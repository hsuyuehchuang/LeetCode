class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0: 
            return -1

        # suffix min
        suf_min = [0] * n
        suf_min[-1] = nums[-1] # boundary, 
        for i in range(n-2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i]) # DP
        
        # prefix max
        curr_max = -1 * float('inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            if curr_max - suf_min[i] <= k:
                return i

        return -1