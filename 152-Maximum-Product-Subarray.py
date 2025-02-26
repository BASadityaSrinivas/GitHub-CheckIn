class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = float('-inf')

        # # Brute-Force
        # for i in range(len(nums)):
        #     curP = nums[i]
        #     maxP = max(maxP, curP)
        #     for j in range(i+1, len(nums)):
        #         curP *= nums[j]
        #         maxP = max(maxP, curP)
        
        # return maxP


        # Optimal - Prefix & Suffix
        maxP = nums[0]
        pre = 1
        suff = 1

        for i in range(len(nums)):
            if pre == 0: pre = 1
            if suff == 0: suff = 1

            pre *= nums[i]
            suff *= nums[len(nums)-1-i]
            maxP = max(maxP, max(pre, suff))
        
        return maxP
