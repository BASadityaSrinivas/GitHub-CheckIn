class Solution:
    def longestPalindrome(self, s: str) -> int:
        even = 0
        odd = 0
        summ = 0

        dic = {}

        for i in s:
            dic[i] = dic.get(i,0) + 1

        for i in dic.values():
            if i%2 == 0:
                even += 1
                summ += i
            else:
                odd += 1
                summ += i 
                summ -= 1
        
        return summ + 1 if odd > 0 else summ