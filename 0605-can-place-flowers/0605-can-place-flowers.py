class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
                0  1  2  3  4  5  6
        arr = [ 0, 0, 1, 0, 0 ], n = 2
                         i
        
        flowers = 

        """

        arr = [0] + flowerbed + [0]
        flowers = 0
        i = 1

        while i < len(arr) - 1:
            if arr[i-1] == 0 and arr[i] == 0 and arr[i+1] == 0:
                flowers+=1
                i += 1
            i += 1
        return flowers >= n


            

        