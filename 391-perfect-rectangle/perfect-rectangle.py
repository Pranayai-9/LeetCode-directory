class Solution:
    def isRectangleCover(self, rectangles):
        if not rectangles:
            return False
        
        # Track the large bounding box boundaries
        x1, y1 = float('inf'), float('inf')
        x2, y2 = float('-inf'), float('-inf')
        
        total_area = 0
        corners = set()
        
        for rx1, ry1, rx2, ry2 in rectangles:
            # Update the perfect bounding box size
            x1, y1 = min(x1, rx1), min(y1, ry1)
            x2, y2 = max(x2, rx2), max(y2, ry2)
            
            # Keep running sum of individual areas
            total_area += (rx2 - rx1) * (ry2 - ry1)
            
            # Apply symmetric difference (XOR) logic for corners
            for corner in [(rx1, ry1), (rx1, ry2), (rx2, ry1), (rx2, ry2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
                    
        # Define the exact 4 expected outer corners
        expected_corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
        
        # The internal corners must cancel out perfectly, leaving only the outer 4
        if corners != expected_corners:
            return False
            
        # The sum of small areas must perfectly match the large bounding box area
        return total_area == (x2 - x1) * (y2 - y1)
