class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        hash_map = {}
        for index,val in enumerate(nums2):
            hash_map[val] = index
        for num in nums1:
            answer.append(hash_map[num])
        return answer
             