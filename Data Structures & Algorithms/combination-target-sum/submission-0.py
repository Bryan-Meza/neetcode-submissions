from collections import deque
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(nums, start, remaining, path):
            if remaining == 0:
                ans.append(path[:])
                return
            for i in range(start, len(nums)):
                num = nums[i]
                if remaining - num < 0:
                    continue
                dfs(nums, i, remaining - num, path + [num])

        dfs(nums, 0, target, [])

        return ans
             

