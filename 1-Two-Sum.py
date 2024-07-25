class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dictt:
                return [i, dictt[diff]]

            if nums[i] not in dictt:
                dictt[nums[i]] = i
