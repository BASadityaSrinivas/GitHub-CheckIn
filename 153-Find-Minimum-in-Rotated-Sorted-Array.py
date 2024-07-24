def binary_search (arr, l, r):
    if l < r:
        mid = (l+r)//2

        if arr[mid] > arr[r]:
            return binary_search(arr, mid + 1, r)
        else:
            return binary_search(arr, l, mid)
    return arr[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return binary_search(nums, 0, len(nums)-1)
        