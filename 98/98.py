# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
         # track max and min val
        upper = float('inf')
        lower = float('-inf')
        # use recursion method
        return self.helper(root,upper,lower)
        
    def helper(self,node,upper,lower):
        #base case
        if not node :
            return True
        val = node.val
        if val <= lower or val >= upper :
            return False
        return self.helper(node.left,val,lower) and self.helper(node.right,upper,val)