"""

level_nodes = 1

que = [ ]

curr_node = [7]

res = [ [3], [9, 20], [15, 7] ]

Output: [ [3], [9,20], [15,7] ]

if just one node return the node
no root, return empty

"""

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = [[root.val]]
        que = deque()
        que.append(root)

        """

        res = [ [3], [9,20], [15,7] ]

        temp = [ 15, 7 ]

        que = [ ]

        node = 

        """

        while que:

            temp = []

            for i in range(len(que)):

                node = que.popleft()

                if node.left:
                    que.append(node.left)
                    temp.append(node.left.val)

                if node.right:
                    que.append(node.right)
                    temp.append(node.right.val)
            
            if len(temp) > 0:
                res.append(temp)
        
        return res
            



        