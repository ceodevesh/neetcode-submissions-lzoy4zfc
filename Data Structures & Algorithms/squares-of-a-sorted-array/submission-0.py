class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        arr = [0]*len(nums)
        writer_index = len(nums)-1
        while i <= j:
            if nums[i]**2 > nums[j]**2:
                arr[writer_index] = nums[i]**2
                i+=1
                writer_index-=1
            else:
                arr[writer_index] = nums[j]**2
                j-=1
                writer_index-=1

        return arr


        