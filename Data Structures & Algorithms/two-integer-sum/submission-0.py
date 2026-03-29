class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_1 = {}
        for i,n in enumerate(nums):
            need = target - n
            if need in hash_1:
                return [hash_1[need], i]
            hash_1[n] = i 