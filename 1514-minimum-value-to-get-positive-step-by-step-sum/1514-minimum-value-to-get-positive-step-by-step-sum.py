class Solution:
    def minStartValue(self, nums):

        """

        nums = [ 1, 2 ]
                 i
 
        min_val = 0
        sum = 0

        
        """
        
        min_val = 0
        sum = 0
        
        for num in nums:
            sum += num
            min_val = min(sum, min_val)
            
        return abs(min_val) + 1

            