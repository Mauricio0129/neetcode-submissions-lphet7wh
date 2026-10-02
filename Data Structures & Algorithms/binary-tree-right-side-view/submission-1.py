# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, 1, 0, [])[1]

    def helper(self, root, current, biggest, res):
        if not root:
            return biggest, res

        print("current:", current, "biggest:", biggest, res)
        if current > biggest:
            biggest = current
            res.append(root.val)


        biggest = self.helper(root.right, current + 1, biggest, res)[0]
        biggest = self.helper(root.left, current + 1, biggest, res)[0]


        return biggest, res
