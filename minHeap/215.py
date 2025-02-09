'''
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # reasigning k
        k = len(nums) - k

        # recursive function
        def quickSelect(l, r):
            # create a pivot and a pointer
            pivot, p = nums[r], l
            # iterate the array except r
            for i in range(l, r):
                # if i th value is less than pivot
                if nums[i] <= pivot:
                    # swap p th and i th value
                    nums[p], nums[i] = nums[i], nums[p]
                    # increament p
                    p += 1
            # now the last swap of p th value with r th or pivot value
            nums[p], nums[r] = nums[r], nums[p]

            # if p is greater than k then k lies on rhs of partition
            if p > k:   return quickSelect(l, p-1)
            # if p is less than k the lies LHS of partition
            if p < k:   return quickSelect(p + 1, r)
            # else just return p
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1)