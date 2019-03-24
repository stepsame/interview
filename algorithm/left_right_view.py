# coding: utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路：层序遍历 再处理

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        cur_nodes = [root]
        result = []
        while cur_nodes:
            result.append([n.val for n in cur_nodes])
            next_nodes = []
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes
        return [r[-1] for r in result]



