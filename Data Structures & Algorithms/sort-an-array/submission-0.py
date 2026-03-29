class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)):
            current_num = nums[i]
            j=i-1
            while j >=0 and nums[j] > current_num:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = current_num
        return nums 

        
        