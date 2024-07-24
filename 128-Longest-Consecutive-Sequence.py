class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 1
        nums_set = set(nums)

        if len(nums) < 1:
            return 0

        for i in nums:
            prev_ele = i - 1
            next_ele = i + 1
            max_count = 1
            
            if prev_ele in nums_set:
                continue
                
            while True:
                if next_ele in nums_set:
                    max_count += 1
                    next_ele += 1
                else:
                    res = max(res, max_count)
                    break
        
        return res
                    

        
            

