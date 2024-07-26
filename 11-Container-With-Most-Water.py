class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxm = 0

        while l < r:
            maxm = max(maxm, min(height[l], height[r])*(r-l))

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
            
        return maxm

        