class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(start, remaining, path):
            if remaining == 0:
                ans.append(path)
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                if remaining - num < 0:
                    continue
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                dfs(i + 1, remaining - num, path + [num])

                

        dfs(0, target, [])

        return ans