class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temperature:
                j, temp2 = stack.pop()
                res[j] = index - j
            stack.append((index, temperature))
        return res
        