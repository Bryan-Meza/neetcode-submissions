class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        timeSlots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))

        heapq.heapify(timeSlots)

        while len(timeSlots) > 1:
            start1, end1 = heapq.heappop(timeSlots)
            start2, end2 = timeSlots[0]

            if end1 >= start2 + duration:
                return [start2, start2 + duration]

        return []