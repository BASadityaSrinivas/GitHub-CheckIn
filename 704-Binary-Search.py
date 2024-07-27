class Solution:
    def binary_search(self, arr, l, r, target):
        m = (l+r)//2
        if arr[m] == target:
            return m
        elif l >= r:
            return -1
        elif arr[m] < target:
            return self.binary_search(arr, m+1, r, target)
        else:
            return self.binary_search(arr, l, m-1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)

        