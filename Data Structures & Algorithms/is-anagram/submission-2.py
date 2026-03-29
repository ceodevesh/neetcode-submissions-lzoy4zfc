class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}

        if len(s) !=len(t):
            return False
        
        for i in range(len(s)):
            count1[s[i]] = count1.get(s[i],0)+1
            count2[t[i]] = count2.get(t[i],0)+1
        
        for j in count1:
            if count1[j] != count2.get(j,0):
                return False
        return True
        

        