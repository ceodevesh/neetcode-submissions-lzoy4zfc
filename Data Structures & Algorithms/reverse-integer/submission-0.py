class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x<0
        x_list = list(str(abs(x)))
        i = 0
        j = len(x_list)-1

        while i <j:
            x_list[i],x_list[j] = x_list[j],x_list[i]
            i+=1
            j-=1
        rev = int("".join(x_list))
        if is_neg:
            rev = -1*rev
        if rev > 2**31 -1 or rev < -2**31:
            return 0
        return  rev
        