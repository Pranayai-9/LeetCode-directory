class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Return empty list immediately if input is empty
        if not digits:
            return []
            
        # Map each phone digit to its corresponding letters
        phone_map = {
            "2": "abc", "3": "def",  "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        combinations = []
        
        def backtrack(index, current_string):
            # Base case: if the current combination is complete
            if len(current_string) == len(digits):
                combinations.append(current_string)
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]
            
            # Loop through all possible letters for this digit
            for letter in possible_letters:
                # Move to the next digit with the updated string
                backtrack(index + 1, current_string + letter)
                
        # Start the backtracking process from index 0 with an empty string
        backtrack(0, "")
        return combinations
