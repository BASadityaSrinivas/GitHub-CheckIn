class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # arr = [False] * (len(nums)+1)

        # for i in nums:
        #     if not arr[i]:
        #         arr[i] = True
        #     else:
        #         return i

        # sett = set()

        for i in nums:
            if i in sett:
                return i
            sett.add(i)
