from bst import TreeNode, BST


class TreeNode(TreeNode):
    def __init__(self, value):
        assert value != None, "You can't use None as a value!!"
        self.data = value
        self.parent = None
        self.left = None
        self.right = None

    def set_left(self, new_node):
        self.left = new_node
        self.left.parent = self

    def set_right(self, new_node):
        self.right = new_node
        self.right.parent = self


class AVL(BST):
    def __init__(self, value):
        self.root = TreeNode(value)

    def rotate_left(self, start_node):
        middle = start_node.right
        middle.parent = start_node.parent
        start_node.right = None
        middle.set_left(start_node)
        return middle

    def rotate_right(self, start_node):
        middle = start_node.left
        middle.parent = start_node.parent
        start_node.left = None
        middle.set_right(start_node)
        return middle

    def rotate_left_right(self, start_node):
        middle = start_node.left.right
        middle.parent = start_node.parent
        start_node.left.right = None
        middle.set_left(start_node.left)
        start_node.left = None
        middle.set_right(start_node)
        return middle

    def rotate_right_left(self, start_node):
        middle = start_node.right.left
        middle.parent = start_node.parent
        start_node.right.left = None
        middle.set_right(start_node.right)
        start_node.right = None
        middle.set_left(start_node)
        return middle


if __name__ == "__main__":
    # to test left rotation
    avl = AVL(1)
    avl.root.set_right(TreeNode(2))
    avl.root.right.set_right(TreeNode(3))
    avl.root.right.right.set_right(TreeNode(4))
    avl.root.right.right.right.set_right(TreeNode(5))
    print(avl, '\n')
    avl.root = avl.rotate_left(avl.root)
    avl.root.right = avl.rotate_left(avl.root.right)
    print(avl)
    print('='*50)

    # to test right rotation
    avl = AVL(1)
    avl.root.set_left(TreeNode(2))
    avl.root.left.set_left(TreeNode(3))
    avl.root.left.left.set_left(TreeNode(4))
    avl.root.left.left.left.set_left(TreeNode(5))
    print(avl, '\n')
    avl.root = avl.rotate_right(avl.root)
    avl.root.left = avl.rotate_right(avl.root.left)
    print(avl)
    print('='*50)

    # to test left-right rotation
    avl = AVL(1)
    avl.root.set_left(TreeNode(2))
    avl.root.left.set_right(TreeNode(3))
    print(avl, '\n')
    avl.root = avl.rotate_left_right(avl.root)
    print(avl)
    print('='*50)
    
    # to test right-left rotation
    avl = AVL(1)
    avl.root.set_right(TreeNode(2))
    avl.root.right.set_left(TreeNode(3))
    print(avl, '\n')
    avl.root = avl.rotate_right_left(avl.root)
    print(avl)
    print('='*50)
    