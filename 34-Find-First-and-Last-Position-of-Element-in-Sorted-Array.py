class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l = 0
        r = len(nums)-1
        leftmost, rightmost = -1, -1

        while l <= r:
            m = (l+r)//2        
                
            if nums[m] == target:
                rightmost = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)//2
            
            if nums[m] == target:
                leftmost = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return [leftmost, rightmost]
                