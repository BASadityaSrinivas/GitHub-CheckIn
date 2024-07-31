class Solution:
    def countKeyChanges(self, s: str) -> int:
        lc = ""
        count = 0

        for ind, c in enumerate(s):
            if ind == 0:
                lc = c
                continue
            if lc == c or lc == chr(ord(c)-32) or lc == chr(ord(c)+32):
                continue
            else:
                count += 1
                lc = c
        
        return count

            