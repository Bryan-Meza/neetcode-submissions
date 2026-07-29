class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        values_dict = {}

        for num in nums:
            if num in values_dict:
                values_dict[num] += 1
            else:
                values_dict[num] = 1

        for index, value in values_dict.items():
            if value > 1:
                return index

        
        