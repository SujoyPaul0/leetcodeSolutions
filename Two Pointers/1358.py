class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hMap = collections.defaultdict(list)
        default = [0, 0, 0]
        for i, ch in enumerate(s):
            if ch == "a":
                default[0] += 1
            elif ch == "b":
                default[1] += 1
            else:
                default[2] += 1
            hMap[i] = default[:]

        l = 0
        r = l + 2
        count = 0
        while r < len(s):
            if l > 0:
                if (hMap[r][0]-hMap[l-1][0]) >= 1 and (hMap[r][1]-hMap[l-1][1]) >= 1 and (hMap[r][2]-hMap[l-1][2]) >= 1:
                    count += len(s) - r
                    l += 1
                else:
                    r += 1
            else:
                if hMap[r][0] >= 1 and hMap[r][1] >= 1 and hMap[r][2] >= 1:
                    count += len(s) - r
                    l += 1
                else:
                    r += 1

        return count
            
        