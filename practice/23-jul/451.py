class Solution:
    def frequencySort(self, s: str) -> str:
        sCount = Counter(s)
        resA = []
        res = ''
        sorted_sCount = dict(sorted(sCount.items(), key=lambda item: -item[1]))

        for key, value in sorted_sCount.items():
            res += key * value

        return res


