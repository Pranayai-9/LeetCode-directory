class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        weight = 0
        decks = pow(n,2)
        con = 0
        while weight < maxWeight and decks != 0:
            weight += w
            if weight > maxWeight:
                break
            decks -= 1
            con += 1
        return con


#Optimized code maxweight/w as constraint:
class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        weight = 0
        deck = pow(n,2)
        con = 0
        limit = maxWeight/w
        if limit >= deck:
            return deck
        else:
            return limit 
    

            



        
               



        
        
