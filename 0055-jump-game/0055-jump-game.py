class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1

        i = len(nums) - 2

        while i >= 0:
            if (nums[i] == 0):
                i -= 1
                continue

            for j in range(1, nums[i] + 1):
                if (dp[i + j] == 1):
                    dp[i] = 1
                    break

            i -= 1

        return dp[0]
