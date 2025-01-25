class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums, target, l, h):
            m = (l+h)//2

            if l > h:
                return -1

            if nums[m] == target:
                return m
            elif nums[m] < target:
                return bs(nums, target, m+1, h)
            else:
                return bs(nums, target, l, m-1)
        
        return bs(nums, target, 0, len(nums)-1)
