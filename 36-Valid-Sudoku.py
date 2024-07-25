class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ## Own solution

        for i in range(9):
            sett1 = set()
            sett2 = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in sett1:
                    return False
                else:
                    sett1.add(board[i][j])
                if board[j][i] != '.' and board[j][i] in sett2:
                    return False
                else:
                    sett2.add(board[j][i])
                    
        boxH = 0
        boxV = 0

        while boxH < 9:
            boxV = 0
            while boxV < 9:
                sett1 = set()
                for i in range(boxV, boxV + 3):
                    for j in range(boxH, boxH + 3):
                        if board[i][j] != '.' and board[i][j] in sett1:
                            return False
                        else:
                            sett1.add(board[i][j])
                boxV += 3   
            boxH += 3

        return True
        