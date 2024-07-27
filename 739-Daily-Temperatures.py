class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, a in enumerate(temperatures):
            while stack and a > temperatures[stack[-1]]:
                stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append(i)
        return res