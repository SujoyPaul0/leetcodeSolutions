class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        sArray = []
        tArray = []
        
        for ch in s:
            sArray.append(ord(ch))
        for ch in t:
            tArray.append(ord(ch))

        l = 0
        max_window = 0
        cost = 0
        for r in range(len(sArray)):
            cost += abs(sArray[r] - tArray[r])

            if cost <= maxCost:
                max_window = max(max_window, r - l + 1)

            while l <= r and cost > maxCost:
                cost -= abs(sArray[l] - tArray[l])
                l += 1
            
        return max_window