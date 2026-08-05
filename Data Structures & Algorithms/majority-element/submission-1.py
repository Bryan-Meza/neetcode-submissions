class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        n = len(nums)

        for num, cnt in count.items():
            if cnt > (n/2):
                return num