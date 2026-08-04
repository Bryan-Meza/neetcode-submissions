class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        l = 1
        for i in range(len(nums)):
            res[i] = l
            l *= nums[i]

        r = 1
        for i in reversed(range(len(nums))):
            res[i] *= r
            r *= nums[i]

        return res