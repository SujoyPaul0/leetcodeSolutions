class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        s = 0
        for f in range(len(nums)):
            if nums[f] != 0 and nums[s] == 0:
                nums[f], nums[s] = nums[s], nums[f]
                
            # if we get 0,0 the wait untill
            # we found non-zero to swap
            if nums[s] != 0:
                s += 1