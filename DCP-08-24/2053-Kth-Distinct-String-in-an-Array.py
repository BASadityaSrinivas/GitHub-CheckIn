class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # sett = set()
        # duplicate_elem = set()

        # for i in arr:
        #     if i in sett:
        #         sett.remove(i)
        #         duplicate_elem.add(i)
        #     elif i not in duplicate_elem:
        #         sett.add(i)
        
        # for i in arr:
        #     if i in sett:
        #         k -= 1
            
        #     if k==0:
        #         return i
        #         break
        
        # return ""

        dic = {}

        for i in arr:
            dic[i] = 1 + dic.get(i, 0)

        for i in arr:
            if dic[i] == 1:
                k -= 1
            if k==0:
                return i

        return ""