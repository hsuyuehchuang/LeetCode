class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if not nums:
            return 0

        def is_Prime(num):
            if num < 2: return False
            if num == 2: return True
            if num % 2 == 0: return False
            for n in range(3, int(num**0.5)+1, 2):
                if num % n == 0:
                    return False
            return True
        
        max_val = max(nums)
        limit = max_val + 100
        
        is_prime_table = []
        for i in range(limit + 1):
            if is_Prime(i):
                is_prime_table.append(True)
            else:
                is_prime_table.append(False)

        total_op = 0
        for idx, val in enumerate(nums):
            curr = val
            if idx % 2 == 0: # even number, should be prime,
                while not is_prime_table[curr]: # FALSE keep going
                    curr += 1
                total_op += (curr - val) # calculate total operation
            else: # odd number, should not be prime
                while is_prime_table[curr]: # TRUE keep going
                    curr += 1
                total_op += (curr - val) # calculate total operation
                
        return total_op        