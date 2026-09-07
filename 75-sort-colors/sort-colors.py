class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Pointers for the boundaries of 0s and 2s
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap with low pointer to move 0 to the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in the right zone, just move forward
                mid += 1
            else: # nums[mid] == 2
                # Swap with high pointer to move 2 to the back
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
