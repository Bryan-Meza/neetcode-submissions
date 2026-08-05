class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        n = len(nums)

        count = Counter(nums)

        for val, cant in count.items():
            if cant > (n/3):
                res.append(val)

        return res  