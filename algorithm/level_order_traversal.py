# coding: utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：记录当前层和下一层

class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if root is None:
            return []
        cur_nodes = [root]
        while cur_nodes:
            result.append([n.val for n in cur_nodes])
            next_nodes = []
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes
        return result


def test():
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a1.left, a1.right = a2, a3
    a2.right = a4
    s = Solution()
    print(s.levelOrder(a1))

if __name__ == '__main__':
    test()
