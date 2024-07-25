class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        og_res = []

        for i in strs:
            srtd = ''.join(sorted(i))
            if srtd in res:
                res[srtd].append(i)
            else:
                res[srtd] = [i]     

        return res.values()