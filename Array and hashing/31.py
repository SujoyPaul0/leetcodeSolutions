class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the break point where two ele are not in inc order
        idx = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                idx = i
                break

        # if idx remains -1 then we just reverse the array as it is in the last permutation
        if idx == -1:
            nums.reverse()
            return nums

        # swap the next bigger element of breakpoint
        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        nums[idx + 1:] = sorted(nums[idx + 1:])

