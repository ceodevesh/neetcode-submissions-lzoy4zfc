class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer_index = 1
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[writer_index] = nums[i]
                writer_index+=1
        return writer_index
        