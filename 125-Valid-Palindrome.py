class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## Two pointer approach

        lp = 0
        rp = len(s)-1

        while rp > lp:
            if s[lp].isalnum():
                if s[rp].isalnum():
                    if s[lp].lower() == s[rp].lower():
                        rp -= 1
                        lp += 1
                    else:
                        return False
                else:
                    rp -= 1
            else:
                lp += 1

        return True
