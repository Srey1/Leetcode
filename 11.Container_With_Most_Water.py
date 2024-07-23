class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maximum = -1
        while i < j:
            volume = (j - i) * min(heights[i], heights[j])
            if volume > maximum:
                maximum = volume
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maximum