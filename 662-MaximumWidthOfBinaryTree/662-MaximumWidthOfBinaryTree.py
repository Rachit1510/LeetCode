# Last updated: 11/3/2025, 9:24:59 PM

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leftmost={}
        max_width=0

        def dfs(node,depth,index):
            nonlocal max_width
            if not node:
                return None
            
            if depth not in leftmost:
                leftmost[depth]=index
            
            current_width= index-leftmost[depth]+1

            max_width=max(max_width,current_width)

            dfs(node.left,depth+1,2*index)
            dfs(node.right,depth+1,2*index+1)
        
        dfs(root,0,0)
        return max_width
        

