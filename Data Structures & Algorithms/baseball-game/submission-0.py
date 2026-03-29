class Solution:
    def calPoints(self, operations: List[str]) -> int:
        set1=[]
        for i in operations:
            if i=="C":
                set1.pop()
            elif i=="D":
                set1.append(set1[-1]*2)
            elif i =="+":
                set1.append(set1[-1]+set1[-2])
            else:
                set1.append(int(i))
        return sum(set1)


        