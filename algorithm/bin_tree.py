# coding: utf-8

# 树的遍历 先序遍历 中序遍历 后序遍历

class BinTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinTree:
    def __init__(self, root):
        self.root = root


def preorder_trav(tree_node):
    if tree_node is not None:
        print(tree_node.val)
        preorder_trav(tree_node.left)
        preorder_trav(tree_node.right)

def inorder_trav(tree_node):
    if tree_node is not None:
        inorder_trav(tree_node.left)
        print(tree_node.val)
        inorder_trav(tree_node.right)



def postorder_trav(tree_node):
    if tree_node is not None:
        postorder_trav(tree_node.left)
        postorder_trav(tree_node.right)
        print(tree_node.val)



def test_bin_tree():
    """
          1
         / \
        2   3
        /    \
       4      5
    :return:
    """
    n1 = BinTreeNode(1)
    n2 = BinTreeNode(2)
    n3 = BinTreeNode(3)
    n4 = BinTreeNode(4)
    n5 = BinTreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.right = n5
    t = BinTree(n1)
    print('pre order')
    preorder_trav(t.root)
    print('in order')
    inorder_trav(t.root)
    print('post order')
    postorder_trav(t.root)

if __name__ == '__main__':
    test_bin_tree()


