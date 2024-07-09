def longestConsecutive(self, nums: List[int]) -> int:
    my_set = set(nums)
    max_length = 0
    for i in  my_set:
        count = 1
        if (i-1) not in my_set:
            while (count + i in nums):
                count += 1
            max_length = max(max_length, count)
    return max_length