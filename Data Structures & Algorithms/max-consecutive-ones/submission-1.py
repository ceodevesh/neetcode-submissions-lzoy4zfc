class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr+=1
            else:
                final = max(final,curr)
                curr = 0
        return max(final,curr)
        