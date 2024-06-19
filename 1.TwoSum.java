class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> findNums = new HashMap<>();
        int difference;
        
        for(int i = 0; i < nums.length; i++) {
            difference = target - nums[i];
            if (findNums.containsKey(difference)) {
                return new int[] {i, findNums.get(difference)};
            }
            else {
                findNums.put(nums[i], i);
            }
        }
    throw new IllegalArgumentException();
    }
}