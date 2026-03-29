class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        g_max = nums[0]
        for i in range (1,len(nums)):
            curr = max(nums[i],curr+nums[i])
            g_max = max(g_max,curr)
        return g_max

            

        