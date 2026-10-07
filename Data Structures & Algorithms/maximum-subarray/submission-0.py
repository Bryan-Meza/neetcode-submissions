class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = bestSum = nums[0]

        for num in nums[1:]:
            cur = max(num, cur + num)
            bestSum = max(bestSum, cur)

        return bestSum