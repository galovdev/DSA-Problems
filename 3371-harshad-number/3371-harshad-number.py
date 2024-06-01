class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        
        get the sum of the integer
        check if the integer is divisible by them

        18 // 10 = 1
        18 % 10 = 8
        
        """

        num = x # 123
        sum = 0 # 6

        while num > 0:
            sum += num % 10
            num = num // 10

        return sum if x % sum == 0 else -1



        