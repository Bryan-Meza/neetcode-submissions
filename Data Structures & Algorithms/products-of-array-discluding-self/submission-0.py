class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * len(nums)

        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(n)):
            res[i] *= right
            right *= nums[i]

        return res

