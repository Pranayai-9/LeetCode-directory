class Solution(object):
    def decimalRepresentation(self,n):
        s=str(n)
        ans=[]
        length=len(s)

        for i in range(length):
            digit=int(s[i])

            if digit!=0:
                ans.append(digit*(10**(length-i-1)))

        return ans
