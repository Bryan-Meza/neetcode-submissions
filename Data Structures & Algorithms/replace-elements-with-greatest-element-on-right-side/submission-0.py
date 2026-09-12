class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        max_num = -1

        for i in reversed(range(len(arr))):
            temp = arr[i]
            arr[i] = max_num
            max_num = max(max_num, temp)
        
        return arr