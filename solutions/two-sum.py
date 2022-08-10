class Solution:
    def twoSum(self, nums : list, target : int):
        for idx in range(len(nums)):
            remainder : int = target - nums[idx]
            try:
                ridx : int = nums.index(remainder, idx+1)
            except ValueError:
                continue
            return [idx, ridx]