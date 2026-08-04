class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsSet = {}

        for i in range(len(nums)):
            if nums[i] in numsSet:
                if abs(i - numsSet[nums[i]]) <= k:
                    return True
            numsSet[nums[i]] = i

        return False