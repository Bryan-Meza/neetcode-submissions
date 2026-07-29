class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for i in range(len(nums)):
            if nums[i] in freqs:
                freqs[nums[i]] += 1
            else:
                freqs[nums[i]] = 1

        arr = []
        for key, value in freqs.items():
            arr.append([value, key])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res