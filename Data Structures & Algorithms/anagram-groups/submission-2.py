class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict()

        for word in strs:
            sortedS = "".join(sorted(word))
            if sortedS not in res:
                res[sortedS] = []
            res[sortedS].append(word)

        return list(res.values())