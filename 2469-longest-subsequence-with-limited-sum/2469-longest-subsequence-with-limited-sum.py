"""

- Given an Integer array, nums 
- Given an Integer array, queries

- Return an array answer of the same size as n
- answer[i] = 

- If all the numbers are bigger than 1 return 0
- At least one query
- Positive numbers 

- approach -
                                   0
nums = [ 4, 5, 6 ], queries = [ 3, 2 ]
         j                      i               
        
pfx = [ 4, 9, 15 ]
        i 

answer = [ 2, 3, 4, 3 ]                      
  
Output: [ 2, 3, 4 ]

-------

nums = [ 4, 5, 2, 1 ]

queries = [ 3, 10, 21 ]
                    q            

pfx = [ 1, 3, 7, 12 ]
                 i

answer = [ 2, 3, 4 ]

1. 

"""

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pfx = []
        answer = []
        pfx_sum = 0
        nums_sorted = sorted(nums)  


        for num in nums_sorted: 
            pfx_sum += num
            pfx.append(pfx_sum)

        for query in queries:
            if query < pfx[0]:
                answer.append(0)
            else:

                for i in range(len(pfx)):
                    if i + 1 == len(pfx) or pfx[i + 1] > query:  
                        answer.append(i + 1)
                        break

        return answer

                


        