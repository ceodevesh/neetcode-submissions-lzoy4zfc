class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,candi = 0 , None

        for i in range(len(nums)):
            if count == 0:
                candi = nums[i]
            if candi == nums[i]:
                count+=1
            else:
                count-=1
        return candi
        