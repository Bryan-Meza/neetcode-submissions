class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        store = set(range(1, n + 1))

        for num in nums:
            if num in store:
                store.discard(num)

        return list(store)