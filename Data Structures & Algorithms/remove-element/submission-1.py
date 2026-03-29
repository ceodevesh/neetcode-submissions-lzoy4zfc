class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        write_index = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[write_index] = nums[i]
                k+=1
                write_index+=1
        return k
        



        