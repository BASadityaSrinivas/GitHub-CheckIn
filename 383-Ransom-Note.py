class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        m = [0] * 26

        for i in magazine:
            m[ord(i)-ord('a')] += 1
        
        for i in ransomNote:
            if m[ord(i)-ord('a')] == 0:
                return False
            m[ord(i)-ord('a')] -= 1
        
        return True




