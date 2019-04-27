# coding: utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：BFS

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        queue, result = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            result.append(cur_level)
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
