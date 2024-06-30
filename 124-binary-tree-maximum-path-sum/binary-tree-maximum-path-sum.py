# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float('inf')
        def getMax(root):
            if not root:
                return 0
            maxLeft = max(getMax(root.left),0)
            maxRight = max(getMax(root.right),0)
            curMax = root.val + maxLeft + maxRight
            self.maxSum = max(self.maxSum, curMax)
            return root.val + max(maxLeft, maxRight)
        
        getMax(root)

        return self.maxSum

          