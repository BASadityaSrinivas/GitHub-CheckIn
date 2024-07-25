class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i+1]:
                continue
            if nums[i] > 0:
                break 
            l, r = i+1, len(nums)-1

            while l < r:
                summ = nums[l] + nums[r] + nums[i]
                if summ == 0:
                    res.add(tup[nums[i], nums[l] , nums[r]]))
                    l += 1
                    r -= 1
                elif summ > 0:
                    r -= 1
                else:
                    l += 1

        res_list = []
        for i in res:
            res_list.append(list(i))

        # print(res_list)

        return res_list