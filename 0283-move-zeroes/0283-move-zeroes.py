class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        lastnonzero=0
        for i in range (len(nums)) :
           if nums[i] != 0 :
             nums[i],nums[lastnonzero] = nums[lastnonzero],nums[i]
             lastnonzero += 1
