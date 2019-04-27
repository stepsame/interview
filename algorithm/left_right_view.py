# coding: utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路：层序遍历 再处理

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode):
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
        return [r[-1] for r in result]