class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}

        res, total, l = 0, 0, 0

        for r in range(len(fruits)):
            if fruits[r] not in count:
                count[fruits[r]] = 1
            else:
                count[fruits[r]] += 1

            total += 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                total -= 1
                l += 1

            res = max(res, total)

        return res