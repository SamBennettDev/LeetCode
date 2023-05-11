public class Solution {
    public int[] RunningSum(int[] nums) {
        int[] sum = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) {
            if (i == 0) {
                sum[i] = nums[i];
                continue;
            }

            sum[i] = sum[i - 1] + nums[i];
        }
        return sum;
    }
}