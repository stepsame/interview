# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        val = preorder.pop(0)
        head = TreeNode(val)
        print(val, inorder)
        index = inorder.index(val)
        head.left = self.buildTree(preorder, inorder[:index])
        head.right = self.buildTree(preorder, inorder[index+1:])
        return head


def test():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    s.buildTree(preorder, inorder)

if __name__ == '__main__':
    test()

