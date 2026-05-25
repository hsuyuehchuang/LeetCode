class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def helper(val, target):
            diff = val % k
            return min((diff - target) % k, (target - diff) % k)

        res = float('inf')
        for x in range(k):
            for y in range(k):
                if x == y: continue

                count = 0
                for i in range(n):
                    if i % 2 == 0:
                        count += helper(nums[i], x)
                    else:
                        count += helper(nums[i], y)
                res = min(res, count)
        return res

