class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        while l <= len(nums) - k:
            r = l + k - 1
            consecutive = True
            maxi = nums[l]
            for i in range(l+1, r+1):
                if nums[i] - nums[i - 1] != 1:
                    consecutive = False
                maxi = max(maxi, nums[i])

            if consecutive == True:
                res.append(maxi)
            else:
                res.append(-1)
            l += 1

        return res
