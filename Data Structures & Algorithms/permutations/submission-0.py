class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(start_index, path):
            if start_index == n:
                res.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(start_index + 1, path)
                    path.pop()
        dfs(0, [])
        return res