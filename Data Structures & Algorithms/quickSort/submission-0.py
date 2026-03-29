# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSort(pairs,0,len(pairs)-1)
        return pairs
    def _quickSort(self,pairs,start,end):
        if start >= end:
            return 
        pivot = pairs[end]
        i = start 
        for j in range(start,end):
            if pairs[j].key < pivot.key:
                pairs[i],pairs[j] = pairs[j],pairs[i]
                i+=1
        pairs[i],pairs[end]=pairs[end],pairs[i]

        self._quickSort(pairs,start,i-1)
        self._quickSort(pairs,i+1,end)
        