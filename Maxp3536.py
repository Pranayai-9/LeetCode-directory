class Solution(object):
    def maxProduct(self, n):
        num = list(str(n))
        x = [int(x) for x in num]
        product = []
        
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                value = int(num[i]) * int(num[j])
                product.append(value) 
                
        result  = max(product)
        return result 


        
