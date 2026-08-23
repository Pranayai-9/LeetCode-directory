class Solution(object):
    def convert(self, s, numRows):
        # Edge cases: no zigzag possible if 1 row or string is too short
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Step through the string character by character
        for char in s:
            rows[current_row] += char
            
            # Change direction when hitting the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down based on direction flag
            current_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return "".join(rows)
