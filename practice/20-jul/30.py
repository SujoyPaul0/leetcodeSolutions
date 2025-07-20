from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        res = []
        concatArray = []
        perm_words = permutations(words)

        for p in perm_words:
            concatArray.append(''.join(p))

        for w in concatArray:
            idx = s.find(w)

            if idx != -1 and idx not in res:
                res.append(idx)

        return res
        