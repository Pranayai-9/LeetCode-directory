#Iterative looping and removing "0"
class Solution(object):
    def removeZeros(self, n):
        num = list(str(n))
        if "0" not in num:
            return n
        else:
            while "0" in num:
                num.remove("0")
        result = "".join(num)
        return int(result)

        
#Replace function:
def removeZeros(self, n):
        cleaned_str = str(n).replace("0", "")
    
        return int(cleaned_str) if cleaned_str else 0
