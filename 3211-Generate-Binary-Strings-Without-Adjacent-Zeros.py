class Solution:
    def validStrings(self, n: int) -> List[str]:
        arr2 = []

        def recur2(arr, cur):
            if len(cur) == n:
                arr.append(cur)
                return

            if cur[-1:] != '0':
                temp = cur + '0'
                recur2(arr, temp)

            temp = cur + '1'
            recur2(arr, temp)
            
        recur2(arr2, '')
        return arr2
