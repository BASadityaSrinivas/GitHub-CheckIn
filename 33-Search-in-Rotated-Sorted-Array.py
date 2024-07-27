def binary_search(arr, l, r, target):
    if l <= r:
        mid = (l+r)//2
        print(l, mid, r)

        if arr[mid] == target:
            return mid

        if arr[l] <= arr[mid]:
            if target > arr[mid] or target < arr[l]:
                return binary_search(arr, mid + 1, r, target)
            else:
                return binary_search(arr, l, mid - 1, target)
        else:
            if target < arr[mid] or target > arr[r]:
                return binary_search(arr, l, mid - 1, target)
            else:
                return binary_search(arr, mid + 1, r, target)
    return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) > 1:    
            return binary_search(nums, 0, len(nums)-1, target)
        else:
            return 0 if nums[0] == target else -1
        