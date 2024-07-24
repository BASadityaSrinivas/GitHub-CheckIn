class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums_corrected = []

        for n in nums:
            temp = ""
            for i in str(n):
                temp += str(mapping[int(i)])
            nums_corrected.append((int(temp), n))

        nums_corrected.sort(key = lambda x: x[0])
        nums = [x[1] for x in nums_corrected]

        return nums

