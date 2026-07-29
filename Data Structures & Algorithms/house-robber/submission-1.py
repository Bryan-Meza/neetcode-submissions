class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])

        max_profit = 0

        for i in range(2, len(nums)):
            current_house = dp[i -1]
            profit = dp[i - 2] + nums[i]
            dp[i] = max(current_house, profit)

        return dp[-1]