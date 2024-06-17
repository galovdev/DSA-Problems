"""

- ps-

- Given an Integer array, nums
- And an Integer, k
- Return the average of k elements before k and after k
- If less elements, k radius avg is -1
- Return an array avgs of the average of k radius for every idx
- Return the avg truncated to zero 

- exp -

nums = [ 7, 4, 3, 9, 1, 8, 5, 2, 6 ], k = 3
                     i

avg =  [ -1, -1, -1, 5, 4, 4, -1, -1, -1 ]

7 + 4 + 3 = 14
9 + 1 + 8 = 18
32 / 6 = 5

- appch - 
         0  1  2  3  4  5  6  7  8
nums = [ 7, 4, 3, 9, 1, 8, 5, 2, 6 ], k = 3
                     i

         0   1   2   3   4   5   6   7   8
pfx =  [ 7, 11, 14, 23, 24, 32, 37, 39, 45 ], k = 2
                 i

1. Create a prefix array
1. Fill a prefix array
2. Check if the current index has a valid window size (i-k > 0 and i+k < len(nums))
3. If the index has a valid subarray, set the k-radius in the avg list
4. Else set -1

"""

class Solution:
    def getAverages(self, nums, k):
        pfx = [nums[0]]
        # fill the pfx array
        for i in range(1, len(nums)):
            pfx.append(pfx[-1] + nums[i])

        avg = [-1] * len(nums)

        """
                0  1  2  3  4  5
        avg = [ 0, 0, 0, 5, 0, 0, 0, 0 ]
                            i
        k = 3 

                   0   1   2   3   4   5   6   7   8
        prefix = [ 7, 11, 14, 23, 24, 32, 37, 39, 45 ]
                                   i

        """

        for i in range(k, len(nums)-k):
            if i - k == 0:
                avg[i] = pfx[i+k] // (k * 2 + 1)
            else:
                avg[i] = (pfx[i+k] - pfx[i-k-1]) // (k * 2 + 1) # 39-7 // 7
        return avg


                








