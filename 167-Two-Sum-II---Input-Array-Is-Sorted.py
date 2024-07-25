class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            summ = numbers[l] + numbers[r]
            
            if target == summ:
                return [l+1, r+1]
            elif target < summ:
                r -= 1
            else:
                l += 1
        
