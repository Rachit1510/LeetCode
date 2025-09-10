# Last updated: 9/10/2025, 11:38:41 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0 

        def buildBST(low, high):
            if self.i >= len(preorder) or not (low < preorder[self.i] < high):
                return None

            root_val = preorder[self.i]
            self.i += 1
            root = TreeNode(root_val)

            root.left = buildBST(low, root_val)   
            root.right = buildBST(root_val, high) 
            return root

        return buildBST(float("-inf"), float("inf"))
        