class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count1 = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                res = max(res,count1)
                count1=0
            else:
                count1+=1
        return max(res,count1)

        