class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_le(val):
            # Counts number of products less than or equat to val
            count = 0
            for x in nums1:
                if x > 0:
                    # We need y <= val / x
                    count += bisect_right(nums2, val / x)
                elif x < 0:
                    # we need y <= val / x (inequelity flips)
                    target = math.ceil(val / x)
                    count += len(nums2) - bisect_left(nums2, target)
                else: # x == 0
                    if val >= 0:
                        count += len(nums2)
            return count
        
        low, high = -10**10 - 1, 10**10 + 1
        ans = high
        
        while low < high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                ans = mid
                high = mid
            else:
                low = mid + 1
        
        return ans