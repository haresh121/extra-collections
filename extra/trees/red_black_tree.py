"""
Red-Black Tree is a self-balancing BST (Binary Search Tree) which means that
it has a guaranteed height of **O(log(n))** where **n** is the number of nodes
within the tree. Each node in the Red-Black Tree has a color, this color is 
either "Red" or "Black". Hence, the name "Red-Black Tree". The color of the node
is used only to re-balance the tree and has nothing to do with anything else.

So, the following is a simple Red-Black Tree:

.. code-block:: text

           ______13|B______
          /                \\
   _____8|R_             __17|R______
  /         \\          /            \\
1|B_        11|B      15|B         __25|B
    \\                            /
    6|R                         22|R

As we can see, the previous Red-Black Tree is a Bineary Search Tree with an
additional color denoted by either **R** for **r**ed or **B** for **b**lack.
In additional to the BST characteristics, Red-black trees have these additional
characteristics:

- A node is either 'red' or 'black'.
- Root is always 'black'.
- A node is 'red' if it has two 'black' children.
- Any child of a red-node is always 'black'.
- **Black depth**: is the depth of all black nodes.
- **Shortest path**: It is the path from the root to the nearest leaf-node and 
it is equal to the black depth.
- **Longest path**: It is the path from the root to the furthest leaf-node with
alternating red and black nodes. And it can't be bigger than (2*shortest-path).

[image]

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **h** is the height of the red-black tree which equals to **log(n)**.

+--------------------------+----------------------------------------------------+------------+---------+
| Method                   | Description                                        | Worst-case | Optimal |
+==========================+====================================================+============+=========+
| __len__()                | Returns the number of nodes in the red-black tree. | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_empty()               | Checks if the red-black tree is empty.             | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __repr__()               | Represents the red-black tree.                     | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the red-black tree.                  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of the given item.            | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_height()             | Gets the red-black tree's height.                  | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_black_height()       | Gets the red-black tree's black height.            | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_depth()              | Gets the red-black tree's depth.                   | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_nodes_per_level()    | Returns a list of all nodes per level.             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_balanced()            | Checks if the red-black tree is balanced.          | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_perfect()             | Checks if the red-black tree is perfect.           | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_strict()              | Checks if the red-black tree is strict.            | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| count_leaf_nodes()       | Counts all leaf nodes in the red-black tree.       | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| clear()                  | Clears the whole red-black tree instance.          | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| to_list()                | Converts the red-black tree instance to list.      | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| traverse()               | Traverses red-black tree based on given method.    | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| preorder_traverse()      | Traverses red-black tree in an pre-order manner.   | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| inorder_traverse()       | Traverses red-black tree in an in-order manner.    | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| postorder_traverse()     | Traverses red-black tree in an post-order manner.  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| breadth_first_traverse() | Traverses the red-black tree level by level.       | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| depth_first_traverse()   | Traverses red-black tree in an pre-order manner.   | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_min()                | Gets the minimum number in the red-black tree.     | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_max()                | Gets the maximum number in the red-black tree.     | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| insert()                 | Inserts a certain value to the red-black tree.     | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove()                 | Removes a certain value from the red-black tree.   | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+

Class Documentation
===================
Here are all of the public methods that can be used with `RedBlackTree()`
objects:

"""
import warnings
from enum import Enum
from extra.trees.bst import BSTNode, BST




class Color(Enum):
    BLACK = 0
    RED = 1




class RedBlackNode(BSTNode):
    """
    A red-black node is the basic unit for building Red-Black Trees. A red-black
    node must contain a number and a color; this color can be either "red" or
    "black" based on the node's position in the tree. Each red-black tree node
    has either zero, one or two children red-black nodes. 
    """
    __name__ = "extra.RedBlackNode()"


    def __init__(self, value, color=Color.RED):
        """
        Creates a `RedBlackNode()` object which is the basic unit for building 
        `RedBlackTree()` objects!!

        Parameters
        ----------
        value: int or float
            The value to be saved within the `BSTNode()` instance
        color: Enum (default:Color.RED)
            The color of the node, it can be either `Color.RED` or `Color.BLACK`
        
        Raises
        ------
        TypeError: If the given `value` isn't a number.
        ValueError: This can be raised in two cases:
            1. If the given `value` is `None`.
            2. If the given color is neither `Color.RED` nor `Color.BLACK`.
        """
        if color not in {Color.RED, Color.BLACK}:
            raise ValueError(f"Invalid color for `{self.__name__}`!!")
        super().__init__(value)
        self._color = color


    def get_color(self):
        """
        Returns the color of the current `RedBlackNode()` instance.

        Returns
        -------
        Enum:
            The color of the current `RedBlackNode()`.
        """
        return self._color


    def set_color(self, new_color):
        """
        Sets the given color as the color of the current `RedBlackNode()`.

        Parameters
        ----------
        new_color: Color
            The new color of the current `RedBlackNode()`.

        Raises
        ------
        Value If the given color is neither `Color.RED` nor `Color.BLACK`.
        """
        if new_color not in {Color.RED, Color.BLACK}:
            raise ValueError(f"Invalid color for `{self.__name__}`!!")
        self._color = new_color
    

    def __repr__(self):
        """
        Represents `RedBlackNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `RedBlackNode()` instance.
        
        Example
        -------
        >>> x = RedBlackNode(10)
        >>> x
        RedNode(10)
        >>>
        >>> x = RedBlackNode(10, color=Color.BLACK)
        >>> x
        BlackNode(10)
        """
        if self._color == Color.RED:
            return f"RedNode({self._data})"
        elif self._color == Color.BLACK:
            return f"BlackNode({self._data})"


    def _represent(self):
        """
        A helpful function used to represent the node when printing!!
        
        Returns
        -------
        str:
            A string representing the `RedBlackNode()` is a very simple way.
        
        Example
        -------
        >>> x = RedBlackNode(10)
        >>> x
        RedNode(10)
        >>> x._represent()
        10
        >>>
        >>> x = RedBlackNode(10, color=Color.BLACK)
        >>> x
        >>> BlackNode(10)
        >>> x._represent()
        10
        >>> type(x._represent())
        <class 'str'>
        """
        if self._color == Color.RED:
            return str(self._data)+'|R'
        elif self._color == Color.BLACK:
            return str(self._data)+'|B'


    @staticmethod
    def swap(node1, node2):
        """
        A static method to swap the data within the given two `RedBlackNode()`
        instances along with the nodes' color.

        Parameters
        ----------
        node1: TreeNode()
            The first `TreeNode()` instance whose data should be swapped.
        node2: TreeNode()
            The second `TreeNode()` instance whose data should be swapped.

        Raises
        ------
        TypeError: If one of the given instances isn't a `RedBlackNode()`.

        Example
        -------
        >>> x = RedBlackNode(10, color=Color.BLACK)
        >>> y = RedBlackNode(20)
        >>>
        >>> RedBlackNode.swap(x, y)
        >>> x
        RedNode(20)
        >>> y
        BlackNode(10)
        >>>
        >>> TreeNode.swap(x, 10)
        TypeError: Incompitable objects' type preventing swapping!!
        """
        # node1._data, node2._data = node2._data, node1._data
        super().swap(node1, node2)
        node1._color, node2._color = node2._color, node1._color




class RedBlackTree(BST):
    _basic_node = RedBlackNode
    __name__ = "extra.RedBlackTree()"
    

    def __init__(self):
        super().__init__()


    @classmethod
    def from_iterable(cls, iterable):
        #TODO: convert this to classmethod like the one with LinkedList
        # do that after applying clear()
        if not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        if len(iterable) == 0:
            raise ValueError("The given iterable is empty!!")
        rbtree = cls()
        for item in iterable:
            rbtree.insert(item)
        return rbtree
    

    ##############################     HEIGHT     ##############################
    def get_black_height(self):
        """
        Number of black nodes from root till to any leaf node, the root node
        is not counted
        """
        black_height = 0
        start_node = self._root.get_left()
        while(start_node is not None):
            if start_node.get_color() == Color.BLACK:
                black_height += 1
            start_node = start_node.get_left()
        # +1 to include NIL node
        return black_height + 1


    ##############################    INSERTION   ##############################
    def __recolor_case3(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # get basic info
        parent = start_node.get_parent()
        grandparent = parent.get_parent() if parent else None
        # parent is left-child and start_node is left-child
        if parent.is_left_child() and start_node.is_left_child():
            grandparent.set_color(Color.RED)
            parent.set_color(Color.BLACK)
            grandparent = super()._rotate_right(grandparent)
        # parent is left-child and start_node is right-child
        elif parent.is_left_child() and not start_node.is_left_child():
            # first rotation
            parent = super()._rotate_left(parent)
            grandparent.set_left(parent)
            grandparent.set_color(Color.RED)
            # second rotation
            grandparent = super()._rotate_right(grandparent)
            grandparent.set_color(Color.BLACK)
        # parent is right-child and start_node is left-child
        elif not parent.is_left_child() and start_node.is_left_child():
            # first rotation
            parent = super()._rotate_right(parent)
            grandparent.set_right(parent)
            grandparent.set_color(Color.RED)
            # second rotation
            grandparent = super()._rotate_left(grandparent)
            grandparent.set_color(Color.BLACK)
        # parent is right-child and start_node is right-child
        else:
            grandparent.set_color(Color.RED)
            parent.set_color(Color.BLACK)
            grandparent = super()._rotate_left(grandparent)
        return grandparent


    def __recolor(self, start_node):
        """
        Recoloring can be done according to these three cases:

        - case I:   parent is 'black'
        - case II:  parent is 'red' and uncle is 'red'
        - case III: parent is 'red' and uncle is 'black'

        """
        # get basic info
        uncle = start_node.get_uncle()
        parent = start_node.get_parent()
        grandparent = parent.get_parent() if parent else None
        # recolor when node has a grandparent
        if parent is None or grandparent is None:
            return parent if parent else start_node

        # case I
        if parent.get_color() == Color.BLACK:
            #do nothing
            # print("Case I")
            return self._root
        else:
            # case II
            if uncle and uncle.get_color() == Color.RED:
                # print("Case II")
                parent.set_color(Color.BLACK)
                uncle.set_color(Color.BLACK)
                grandparent.set_color(Color.RED)
            # case III
            else:
                # print("Case III")
                # get great grandparent
                great_grandparent = grandparent.get_parent()
                grandparent = self.__recolor_case3(start_node)
                # set connection
                if great_grandparent:
                    if great_grandparent.get_data() > grandparent.get_data():
                        great_grandparent.set_left(grandparent)
                    else:
                        great_grandparent.set_right(grandparent)
            # recursively do the same over grandparent 
            return self.__recolor(grandparent)


    def insert(self, value):
        super()._validate_item(value)
        if self.is_empty():
            self._root = self._basic_node(value)
            self._root.set_color(Color.BLACK)
            self._length += 1
        else:
            # insert new node
            new_node = super()._insert(value)
            # recolor starting from new_node till root
            self._root = self.__recolor(new_node)
            # root is always black (isn't essential tho!!)
            self._root.set_color(Color.BLACK)


    ##############################     REMOVAL    ##############################
    def _find_replacement(self, start_node):
        """
        NOTE: Here, we're tyring to exploit two characteristics of Red-black
        trees and they are: 

            - red-nodes are good replacements.
            - when removing a red node, there must be at least one red-node as \
                a replacement at least.
        """
        assert isinstance(start_node, RedBlackNode)
        if start_node.is_leaf():
            replacement_node = None
        else:
            # in-order successor
            successor = super()._get_min_node(start_node.get_right()) \
                if start_node.get_right() else None
            # in-order predecessor
            predecessor = super()._get_max_node(start_node.get_left()) \
                if start_node.get_left() else None
            # find the red-node
            if successor and successor.get_color() == Color.RED:
                replacement_node = successor
            elif predecessor and predecessor.get_color() == Color.RED:
                replacement_node = predecessor
            else:
                replacement_node = successor if successor else predecessor
        return replacement_node


    def __handle_double_black(self, parent, double_black_node):
        """
        When dealing with double black nodes, we have four cases:
        Case I  : if double_black_node is root
        Case II : (s) is black and one child of sibling's children is red (r)
        Case III: (s) is black and the two children of s are black
        Case IV : (s) is red
        
        Note: (s) is the sibling of the double_black_node
        SRC: https://www.programiz.com/dsa/deletion-from-a-red-black-tree
        """
        #TODO: should be refactored
        assert isinstance(parent, RedBlackNode)
        assert double_black_node is None or \
            isinstance(double_black_node, RedBlackNode)
        
        while double_black_node != self._root and (not double_black_node \
            or double_black_node.get_color() == Color.BLACK):
            # double black node is the left-child
            if double_black_node == parent.get_left():
                sibling = parent.get_right()
                # Case IV
                if sibling and sibling.get_color() == Color.RED:
                    sibling.set_color(Color.BLACK)
                    parent.set_color(Color.RED)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_left(parent)
                    super()._attach(grandparent, parent)
                    # update parent and sibling
                    parent = parent.get_left()
                    sibling = parent.get_right()
                # check sibling children
                s_left_child = sibling.get_left()
                s_right_child = sibling.get_right()
                # get colors of sibling's children
                s_left_color = s_left_child.get_color() if s_left_child \
                                                        else Color.BLACK
                s_right_color = s_right_child.get_color() if s_right_child \
                                                          else Color.BLACK
                # Case III
                if s_left_color==Color.BLACK and s_right_color==Color.BLACK:
                    sibling.set_color(Color.RED)
                    double_black_node = parent
                # Case II
                else:
                    if s_right_color == Color.BLACK:
                        s_left_child.set_color(Color.BLACK)
                        sibling.set_color(Color.RED)
                        sibling = super()._rotate_right(sibling)
                        super()._attach(parent, sibling)
                        sibling = parent.get_right()

                    sibling.set_color(parent.get_color())
                    parent.set_color(Color.BLACK)
                    s_right_child = sibling.get_right()
                    s_right_child.set_color(Color.BLACK)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_left(parent)
                    super()._attach(grandparent, parent)
                    double_black_node = self._root
            ##### Mirror image of the previous if-condition ######
            # double black node is the right-child
            else:
                sibling = parent.get_left()
                # Case IV
                if sibling and sibling.get_color() == Color.RED:
                    sibling.set_color(Color.BLACK)
                    parent.set_color(Color.RED)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_right(parent)
                    super()._attach(grandparent, parent)
                    # update parent and sibling
                    parent = parent.get_right()
                    sibling = parent.get_left()
                # check sibling children
                s_left_child = sibling.get_left()
                s_right_child = sibling.get_right()
                # get colors of sibling's children
                s_left_color = s_left_child.get_color() if s_left_child \
                                                        else Color.BLACK
                s_right_color = s_right_child.get_color() if s_right_child \
                                                          else Color.BLACK
                # Case III
                if s_right_color==Color.BLACK and s_right_color==Color.BLACK:
                    sibling.set_color(Color.RED)
                    double_black_node = parent
                # Case II
                else:
                    if s_left_color == Color.BLACK:
                        s_right_child.set_color(Color.BLACK)
                        sibling.set_color(Color.RED)
                        sibling = super()._rotate_left(sibling)
                        super()._attach(parent, sibling)
                        sibling = parent.get_left() 

                    sibling.set_color(parent.get_color())
                    parent.set_color(Color.BLACK)
                    s_left_child = sibling.get_left()
                    s_left_child.set_color(Color.BLACK)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_right(parent)
                    super()._attach(grandparent, parent)
                    double_black_node = self._root
        # make sure root is always black
        self._root.set_color(Color.BLACK)


    def remove(self, del_value):
        """
        Case I  : removed_node is 'red', replacement is either 'red' or None
        Case II : removed_node is 'red', replacement is 'black'
        Case III: removed_node is 'black', replacement is either 'black' or None
        Case IV : removed_node is 'black', replacement is 'red'
        """
        # check edge case
        if self.is_empty():
            warnings.warn(f"`{self.__name__}` is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return
        elif self._root.is_leaf() and del_value == self._root.get_data():
            self._root = None
            self._length -= 1
            return

        # search for the del_value node
        removed_node = super()._search(del_value, self._root)
        # couldn't find the node
        if removed_node.get_data() != del_value:
            warnings.warn(f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return
        # find replacement
        replacement = self._find_replacement(removed_node)
        # print("replacement:", replacement)

        # Case I (replace red-node with red-node/None)
        if removed_node.get_color() == Color.RED and \
            (replacement is None or replacement.get_color() == Color.RED):
            # print("Case I (replace red-node with red-node/None)")
            super()._transplant(removed_node, replacement)
        
        # Case II (replace red-node with black-node)
        elif removed_node.get_color() == Color.RED and \
            replacement.get_color() == Color.BLACK:
            # print("Case II (replace red-node with black-node)")
            raise ValueError("Debug this, this case shouldn't occur!!")
        
        # Case III (replace black-node with black-node)
        elif removed_node.get_color() == Color.BLACK and \
            (replacement is None or replacement.get_color() == Color.BLACK):
            # print("Case III (double black-node)")
            if replacement:
                parent = replacement.get_parent()
            else:
                parent = removed_node.get_parent()
            # do the transplant
            super()._transplant(removed_node, replacement)
            # get double black node
            if replacement is None:
                if parent.get_left() is None:
                    double_black_node = parent.get_left()
                else:
                    double_black_node = parent.get_right()
            else:
                if replacement.get_data() < parent.get_data():
                    double_black_node = parent.get_left() 
                else:
                    double_black_node = parent.get_right() 
            # handle this double black
            self.__handle_double_black(parent, double_black_node)
        
        # Case IV (replace black-node with red-node/None)
        elif removed_node.get_color() == Color.BLACK and \
            replacement.get_color() == Color.RED:
            replacement.set_color(Color.BLACK)
            # print("Case IV (replace black-node with red-node/None)")
            super()._transplant(removed_node, replacement)
        # decrease the length
        self._length -= 1
        

