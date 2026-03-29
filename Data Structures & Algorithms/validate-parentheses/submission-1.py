class Solution:
    def isValid(self, s: str) -> bool:
        hash_1 = {")":"(","]":"[","}":"{"}
        new = []
        for i in s:
            if i in hash_1:
                if not new or new[-1]!=hash_1[i]:
                    return False
                new.pop()
            else:
                new.append(i)
        return len(new) == 0