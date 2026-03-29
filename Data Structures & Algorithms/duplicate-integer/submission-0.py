class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1= set()
        for i in range(len(nums)):
            if nums[i] not in set1:
                set1.add(nums[i])
            else:
                return True
        return False 


        