class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pAr = []
        for ch in pattern:
            pAr.append(ch)

        sAr = s.split()
        pMap = {}
        sMap = {}

        if len(pAr) != len(sAr):
            return False

        for p, st in zip(pAr, sAr):
            if p in pMap and pMap[p] != st:
                return False
            if st in sMap and sMap[st] != p:
                return False

            pMap[p] = st
            sMap[st] = p

        return True