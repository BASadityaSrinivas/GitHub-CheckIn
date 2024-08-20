class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1hash = [0] * 26
        s2hash = [0] * 26

        for i in s1:
            s1hash[ord(i)-ord('a')] += 1
        
        for i in range(len(s1)):
            s2hash[ord(s2[i])-ord('a')] += 1

        start = 0
        end = len(s1)-1

        while end < len(s2)-1:
            if s1hash == s2hash:
                return True
            s2hash[ord(s2[start])-ord('a')] -= 1
            start += 1
            end += 1
            s2hash[ord(s2[end])-ord('a')] += 1
        
        if s1hash == s2hash:
            return True

        return False
