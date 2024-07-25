class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            out[i] = nums[i-1] * out[i-1]
        
        p = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            out[i] *= p
            p *= nums[i]
        
        return out