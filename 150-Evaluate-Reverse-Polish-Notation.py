class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNums = []
        for i in tokens:
            if i == '+':
                stackNums.append(stackNums.pop() + stackNums.pop())
            elif i == '-':
                b, a = stackNums.pop(), stackNums.pop()
                stackNums.append(a-b)
            elif i == '*':
                stackNums.append(stackNums.pop() * stackNums.pop())
            elif i == '/':
                b, a = stackNums.pop(), stackNums.pop()
                stackNums.append(int(a/b))
            else:
                stackNums.append(int(i))
        return stackNums[0]
            
