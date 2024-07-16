class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int min = INT_MAX;
        int count = 0;
        int j = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] >= target) {
                return 1;
            }

            count += nums[i];

            for (j; count >= target; j++) {
                if (i - j + 1 < min) {
                    min = i - j + 1;
                }

                count -= nums[j];
            }
        }

        if (min == INT_MAX) {
            return 0;
        }

        return min;
    }
};