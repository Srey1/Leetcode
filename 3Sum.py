class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0,len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                if (nums[left] + nums[right] > -nums[i]):
                    right -= 1
                elif (nums[left] + nums[right] < -nums[i]):
                    left += 1
                else:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res
        