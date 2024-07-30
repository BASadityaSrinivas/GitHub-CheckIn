class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        
        res = 1
        for i in range(len(s)):
            sett = {s[i]}
            for j in range(i+1, len(s)):
                if s[j] in sett:
                    break
                else:
                    sett.add(s[j])
            res = max(res, len(sett))
        
        return res
