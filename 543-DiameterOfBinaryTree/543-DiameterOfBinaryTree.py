# Last updated: 9/6/2025, 9:14:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def height(root):
            nonlocal res
            if not root:
                return 0
            left= height(root.left)
            right= height(root.right)

            res= max(res,left+right)
            return 1+max(left,right)
        height(root)
        return res


        