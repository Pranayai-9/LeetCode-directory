class Solution(object):
    def findMinDifference(self, timePoints):
        # 1. Keep your sorted array approach
        original = sorted(timePoints)
        
        # 2. Keep your exact logic: if any item appears twice, return 0
        for item in timePoints:
            if original.count(item) >= 2:
                return 0
        
        # 3. Convert all sorted string times into minute integers
        minutes = []
        for time in original:
            h, m = map(int, time.split(":"))
            minutes.append(h * 60 + m)
            
        # 4. Loop through ALL adjacent pairs to find the smallest gap
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i-1]
            if diff < min_diff:
                min_diff = diff
                
        # 5. Check the circular wrap-around across midnight
        midnight_diff = (1440 - minutes[-1]) + minutes[0]
        if midnight_diff < min_diff:
            min_diff = midnight_diff
            
        return min_diff
