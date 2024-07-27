class Solution:
    def binary_search_row(self, arr, l, r, target):
        m = (l+r)//2
        if arr[m] == target:
            return True
        elif l >= r:
            return False
        elif arr[m] < target:
            return self.binary_search_row(arr, m+1, r, target)
        else:
            return self.binary_search_row(arr, l, m-1, target)

    def binary_search(self, arr, start_c, end_c, target):
        mid_c = (start_c + end_c) // 2
        if arr[mid_c][0] <= target and target <= arr[mid_c][-1]:
            return self.binary_search_row(arr[mid_c], 0, len(arr[mid_c])-1, target)
        elif start_c >= end_c:
            return False
        elif arr[mid_c][0] > target:
            return self.binary_search(arr, start_c, mid_c-1, target)
        else:
            return self.binary_search(arr, mid_c+1, end_c, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binary_search(matrix, 0, len(matrix)-1, target)