"""
Red-Black Trees are self-balancing BSTs (Binary Search Trees) which means that
they have a guaranteed height of O(log(n)) where n is the number of nodes within
the tree. The color is used only to re-balance trees and has nothing to do with
any thing else.

Red black trees have the following characteristics:
- A node is either 'red' or 'black'.
- Root is always 'black'.
- A node is 'red' if it has two 'black' children.
- Any child of a red-node is always 'black'.

Some other properties:
- "Black depth": is the depth of all black nodes.
- "Shortest path": (from parent to leaf-node) is equal to the black depth.
- "Longest path": is the one with alternating red and black nodes.
- The longest path can't be bigger than (2*shortest-path).

Considering the following BST:
  __B
 /   \
A     C
 \
  Z
We can say that:
- B is parent of A and C
- A and C are children for B
- B is grandparent for Z
- A is parent of Z
- C is uncle of Z (important)
"""
from enum import Enum
from bst import TreeNode, BST


class Color(Enum):
    BLACK = 0
    RED = 1


class TreeNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.color = Color.RED

    def get_color(self):
        return self.color

    def set_color(self, color):
        assert color in {Color.RED, Color.BLACK}, "Invalid color!!"
        self.color = color

    def represent_data(self):
        if self.color == Color.RED:
            return str(self.data)+'r'
        elif self.color == Color.BLACK:
            return str(self.data)+'b'





class RedBlackTree(BST):
    def __init__(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        else:
            self.root = TreeNode(value)
        self.root.color = Color.BLACK


    ############################## ROTATION ##############################
    def __rotate_left(self, start_node):
        # print("Rotating Left")
        middle = start_node.get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle

    def __rotate_right(self, start_node):
        # print("Rotating Right")
        middle = start_node.get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle


    ############################## INSERTION ##############################
    def __insert(self, value):
        # insert new node
        node = super().insert(value)
        parent = node.get_parent()
        # cast into TreeNode with color
        new_node = TreeNode(value)
        new_node.set_color(Color.RED)
        # take care of node-parrent connection
        if value > parent.get_data():
            parent.set_right(new_node)
        elif value < parent.get_data():
            parent.set_left(new_node)
        return new_node


    def insert(self, value):
        """
        When inserting a value, we set color as red and then re-color it
        according to these three cases:
        - case I:   parent is 'black'
        - case II:  parent is 'red' and uncle is 'red'
        - case III: parent is 'red' and uncle is 'black'
        """
        new_node = self.__insert(value)
        # get necessary info
        parent = new_node.get_parent()
        uncle = new_node.get_uncle()
        grand_parent = parent.get_parent()
        # case I
        if parent.get_color() == Color.BLACK:
            pass #do nothing
        else:
            # case II
            if uncle and uncle.get_color() == Color.RED:
                parent.set_color(Color.BLACK)
                uncle.set_color(Color.BLACK)
                grand_parent.set_color(Color.RED)
            # case III
            else:
                # parent is left-child and node is left-child
                if parent.is_left_child() and new_node.is_left_child():
                    grand_parent.set_color(Color.RED)
                    parent.set_color(Color.BLACK)
                    grand_parent = self.__rotate_right(grand_parent)
                # parent is left-child and node is right-child
                elif parent.is_left_child() and not new_node.is_left_child():
                    parent = self.__rotate_left(parent)
                # parent is right-child and node is left-child
                elif not parent.is_left_child() and new_node.is_left_child():
                    parent = self.__rotate_right(parent)
                # parent is right-child and node is right-child
                else:
                    grand_parent.set_color(Color.RED)
                    parent.set_color(Color.BLACK)
                    grand_parent = self.__rotate_left(grand_parent)
        # make sure the root is black
        self.root.set_color(Color.BLACK)







if __name__ == "__main__":
    rbtree = RedBlackTree(8)
    rbtree.insert(5)
    rbtree.insert(15)
    rbtree.insert(12)
    rbtree.insert(19)
    rbtree.insert(9)
    rbtree.insert(13)
    rbtree.insert(23)
    print(rbtree)
