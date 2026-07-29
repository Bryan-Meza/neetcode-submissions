class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l = start of the container
        # r = end of the container
        l, r = 0, len(heights) - 1
        
        # Max Area
        res = 0

        # Continue until two pointers can't advance
        while l < r:
            # formula for the are
            # r - l = width
            # choose min val of l or r = height
            area = (r - l) * min(heights[l], heights[r])
            # result the max value of the
            # saved res or the new area
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

