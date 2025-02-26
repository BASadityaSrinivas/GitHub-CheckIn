class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDic = {}
        n = len(s)
        m = len(t)
        cnt = 0
        l,r = 0,0
        minL = 100000
        si = -1

        for i in t:
            tDic[i] = tDic.get(i, 0) + 1

        while r < len(s):
            if s[r] in tDic and tDic[s[r]] > 0:
                cnt += 1
                tDic[s[r]] = tDic.get(s[r], 0) - 1
            else:
                tDic[s[r]] = tDic.get(s[r], 0) - 1
            # print(l,r,s[l],s[r],cnt)
            
            while cnt == m:
                if (r-l+1 < minL):
                    si = l
                    minL = r-l+1
                # if s[l] in tDic:
                tDic[s[l]] = tDic.get(s[l], 0) + 1
                
                if tDic[s[l]] > 0:
                    cnt -= 1
                l += 1
            
            r += 1
        
        return \\ if si==-1 else s[si:si+minL] 
