import pytest

from extra.trees.red_black_tree import Color, RedBlackNode, RedBlackTree


def test_red_black_node(helper):
    with pytest.raises(TypeError):
        RedBlackNode(None)
        RedBlackNode("  ")
        RedBlackNode(RedBlackTree())
        RedBlackNode(helper.get_string())
        RedBlackNode(helper.get_value())
        RedBlackNode(helper.get_list())
        RedBlackNode(Color.RED)
    # these should raise any erros
    RedBlackNode(helper.get_float())
    assert RedBlackNode(helper.get_float()).get_color() == Color.RED
    RedBlackNode(helper.get_int())
    assert RedBlackNode(helper.get_float()).get_color() == Color.RED
    with pytest.raises(ValueError):
        node = RedBlackNode(helper.get_int())
        node.set_color(0)
        node.set_color(1)
        node.set_color(helper.get_value())


def test_red_black_tree_from_iterable(helper):
    rbtree = RedBlackTree([7, 3, 0])
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 3
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 7
    assert rbtree.get_min() == 0
    assert rbtree.get_height() == 1
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 1
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 3
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 0
    assert rbtree._root.get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left() is None
    assert rbtree._root.get_left().get_right() is None

    assert rbtree._root.get_right().get_data() == 7
    assert rbtree._root.get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_left() is None
    assert rbtree._root.get_right().get_right() is None


def test_red_black_special_case(helper):
    rbtree = RedBlackTree()
    rbtree.insert(15)
    rbtree.insert(5)
    rbtree.insert(1)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 3
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 15
    assert rbtree.get_min() == 1
    assert rbtree.get_height() == 1
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 1
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 5
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 1
    assert rbtree._root.get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left() is None
    assert rbtree._root.get_left().get_right() is None

    assert rbtree._root.get_right().get_data() == 15
    assert rbtree._root.get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_left() is None
    assert rbtree._root.get_right().get_right() is None


def test_red_black_tree_insert_example1(helper):
    # src: https://www.geeksforgeeks.org/red-black-tree-set-2-insert/
    rbtree = RedBlackTree()
    rbtree.insert(10)
    rbtree.insert(20)
    rbtree.insert(30)
    rbtree.insert(15)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 4
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 30
    assert rbtree.get_min() == 10
    assert rbtree.get_height() == 2
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 20
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 10
    assert rbtree._root.get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left() is None
    assert rbtree._root.get_left().get_right().get_data() == 15
    assert rbtree._root.get_left().get_right().get_color() == Color.RED
    assert rbtree._root.get_left().get_right().get_left() is None
    assert rbtree._root.get_left().get_right().get_right() is None

    assert rbtree._root.get_right().get_data() == 30
    assert rbtree._root.get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left() is None
    assert rbtree._root.get_right().get_right() is None


def test_red_black_tree_insert_example2(helper):
    # src: https://www.youtube.com/watch?v=eO3GzpCCUSg
    rbtree = RedBlackTree()
    rbtree.insert(8)
    rbtree.insert(5)
    rbtree.insert(15)
    rbtree.insert(12)
    rbtree.insert(19)
    rbtree.insert(9)
    rbtree.insert(13)
    rbtree.insert(23)
    rbtree.insert(10)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 9
    assert rbtree.count_leaf_nodes() == 4
    assert rbtree.get_max() == 23
    assert rbtree.get_min() == 5
    assert rbtree.get_height() == 3
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2

    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 12
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 8
    assert rbtree._root.get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left().get_data() == 5
    assert rbtree._root.get_left().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left().get_left() is None
    assert rbtree._root.get_left().get_left().get_right() is None
    assert rbtree._root.get_left().get_right().get_data() == 9
    assert rbtree._root.get_left().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left().get_left() is None
    assert rbtree._root.get_left().get_right().get_right().get_data() == 10
    assert (
        rbtree._root.get_left().get_right().get_right().get_color()
        == Color.RED
    )
    assert rbtree._root.get_left().get_right().get_right().get_left() is None
    assert rbtree._root.get_left().get_right().get_right().get_right() is None

    assert rbtree._root.get_right().get_data() == 15
    assert rbtree._root.get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_left().get_data() == 13
    assert rbtree._root.get_right().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right().get_data() == 19
    assert rbtree._root.get_right().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_right().get_data() == 23
    assert (
        rbtree._root.get_right().get_right().get_right().get_color()
        == Color.RED
    )
    assert rbtree._root.get_right().get_right().get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_right().get_right() is None


def test_red_black_tree_insert_example3(helper):
    # src: http://www.btechsmartclass.com/data_structures/red-black-trees.html
    rbtree = RedBlackTree()
    rbtree.insert(8)
    rbtree.insert(18)
    rbtree.insert(5)
    rbtree.insert(15)
    rbtree.insert(17)
    rbtree.insert(25)
    rbtree.insert(40)
    rbtree.insert(80)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 8
    assert rbtree.count_leaf_nodes() == 4
    assert rbtree.get_max() == 80
    assert rbtree.get_min() == 5
    assert rbtree.get_height() == 3
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 17
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 8
    assert rbtree._root.get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left().get_data() == 5
    assert rbtree._root.get_left().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left().get_left() is None
    assert rbtree._root.get_left().get_left().get_right() is None
    assert rbtree._root.get_left().get_right().get_data() == 15
    assert rbtree._root.get_left().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_right().get_left() is None
    assert rbtree._root.get_left().get_right().get_right() is None

    assert rbtree._root.get_right().get_data() == 25
    assert rbtree._root.get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_left().get_data() == 18
    assert rbtree._root.get_right().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right().get_data() == 40
    assert rbtree._root.get_right().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_right().get_data() == 80
    assert (
        rbtree._root.get_right().get_right().get_right().get_color()
        == Color.RED
    )
    assert rbtree._root.get_right().get_right().get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_right().get_right() is None


def test_red_black_tree_insert_example4(helper):
    # src: Data Structures and Algorithms in Python Book (Page: 539)
    rbtree = RedBlackTree()
    rbtree.insert(4)
    rbtree.insert(7)
    rbtree.insert(12)
    rbtree.insert(15)
    rbtree.insert(3)
    rbtree.insert(5)
    rbtree.insert(14)
    rbtree.insert(18)
    rbtree.insert(16)
    rbtree.insert(17)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 10
    assert rbtree.count_leaf_nodes() == 5
    assert rbtree.get_max() == 18
    assert rbtree.get_min() == 3
    assert rbtree.get_height() == 3
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 14
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 7
    assert rbtree._root.get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left().get_data() == 4
    assert rbtree._root.get_left().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left().get_left().get_data() == 3
    assert (
        rbtree._root.get_left().get_left().get_left().get_color() == Color.RED
    )
    assert rbtree._root.get_left().get_left().get_left().get_left() is None
    assert rbtree._root.get_left().get_left().get_left().get_right() is None
    assert rbtree._root.get_left().get_left().get_right().get_data() == 5
    assert (
        rbtree._root.get_left().get_left().get_right().get_color() == Color.RED
    )
    assert rbtree._root.get_left().get_left().get_right().get_left() is None
    assert rbtree._root.get_left().get_left().get_right().get_right() is None
    assert rbtree._root.get_left().get_right().get_data() == 12
    assert rbtree._root.get_left().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_right().get_left() is None
    assert rbtree._root.get_left().get_right().get_right() is None

    assert rbtree._root.get_right().get_data() == 16
    assert rbtree._root.get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_left().get_data() == 15
    assert rbtree._root.get_right().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right().get_data() == 18
    assert rbtree._root.get_right().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_right().get_left().get_data() == 17
    assert (
        rbtree._root.get_right().get_right().get_left().get_color()
        == Color.RED
    )
    assert rbtree._root.get_right().get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right().get_right() is None


def test_red_black_tree_insert_remove_example1(helper):
    # src: https://www.youtube.com/watch?v=eO3GzpCCUSg
    rbtree = RedBlackTree()
    rbtree.insert(5)
    rbtree.insert(2)
    rbtree.insert(8)
    rbtree.insert(1)
    rbtree.insert(4)
    rbtree.insert(7)
    rbtree.insert(9)
    rbtree.remove(2)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 6
    assert rbtree.count_leaf_nodes() == 3
    assert rbtree.get_max() == 9
    assert rbtree.get_min() == 1
    assert rbtree.get_height() == 2
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 5
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 4
    assert rbtree._root.get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left().get_data() == 1
    assert rbtree._root.get_left().get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left().get_left() is None
    assert rbtree._root.get_left().get_left().get_right() is None
    assert rbtree._root.get_left().get_right() is None

    assert rbtree._root.get_right().get_data() == 8
    assert rbtree._root.get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left().get_data() == 7
    assert rbtree._root.get_right().get_left().get_color() == Color.RED
    assert rbtree._root.get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right().get_data() == 9
    assert rbtree._root.get_right().get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_right() is None


def test_red_black_tree_insert_remove_example2(helper):
    # src: https://www.youtube.com/watch?v=eO3GzpCCUSg
    rbtree = RedBlackTree()
    rbtree.insert(7)
    rbtree.insert(3)
    rbtree.insert(18)
    rbtree.insert(10)
    rbtree.insert(22)
    rbtree.insert(8)
    rbtree.insert(11)
    rbtree.insert(26)
    rbtree.remove(3)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 7
    assert rbtree.count_leaf_nodes() == 3
    assert rbtree.get_max() == 26
    assert rbtree.get_min() == 7
    assert rbtree.get_height() == 3
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 18
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 10
    assert rbtree._root.get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left().get_data() == 7
    assert rbtree._root.get_left().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left().get_left() is None
    assert rbtree._root.get_left().get_left().get_right().get_data() == 8
    assert (
        rbtree._root.get_left().get_left().get_right().get_color() == Color.RED
    )
    assert rbtree._root.get_left().get_left().get_right().get_left() is None
    assert rbtree._root.get_left().get_left().get_right().get_right() is None

    assert rbtree._root.get_right().get_data() == 22
    assert rbtree._root.get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_data() == 26
    assert rbtree._root.get_right().get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_right() is None


def test_red_black_tree_insert_remove_example3(helper):
    # src: https://www.youtube.com/watch?v=eO3GzpCCUSg
    rbtree = RedBlackTree()
    rbtree.insert(13)
    rbtree.insert(8)
    rbtree.insert(17)
    rbtree.insert(1)
    rbtree.insert(11)
    rbtree.insert(1)
    rbtree.insert(15)
    rbtree.insert(25)
    rbtree.insert(6)
    rbtree.insert(22)
    rbtree.insert(27)
    rbtree.remove(11)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 9
    assert rbtree.count_leaf_nodes() == 5
    assert rbtree.get_max() == 27
    assert rbtree.get_min() == 1
    assert rbtree.get_height() == 3
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 13
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 6
    assert rbtree._root.get_left().get_color() == Color.RED
    assert rbtree._root.get_left().get_left().get_data() == 1
    assert rbtree._root.get_left().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left().get_left() is None
    assert rbtree._root.get_left().get_left().get_right() is None
    assert rbtree._root.get_left().get_right().get_data() == 8
    assert rbtree._root.get_left().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_right().get_left() is None
    assert rbtree._root.get_left().get_right().get_right() is None

    assert rbtree._root.get_right().get_data() == 17
    assert rbtree._root.get_right().get_color() == Color.RED
    assert rbtree._root.get_right().get_left().get_data() == 15
    assert rbtree._root.get_right().get_left().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right().get_data() == 25
    assert rbtree._root.get_right().get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_right().get_left().get_data() == 22
    assert (
        rbtree._root.get_right().get_right().get_left().get_color()
        == Color.RED
    )
    assert rbtree._root.get_right().get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right().get_right().get_data() == 27
    assert (
        rbtree._root.get_right().get_right().get_right().get_color()
        == Color.RED
    )
    assert rbtree._root.get_right().get_right().get_right().get_left() is None
    assert rbtree._root.get_right().get_right().get_right().get_right() is None


def test_red_black_tree_insert_remove_invalid_examples(helper):
    rbtree = RedBlackTree()
    rbtree.insert(10)
    with pytest.warns(UserWarning):
        rbtree.remove(helper.get_int())
    with pytest.warns(UserWarning):
        rbtree.remove(helper.get_string())
    with pytest.warns(UserWarning):
        rbtree.remove(helper.get_list())
    with pytest.warns(UserWarning):
        rbtree.remove(RedBlackNode(10))
    with pytest.warns(UserWarning):
        rbtree.remove(RedBlackTree())


def test_double_black_left_left_case(helper):
    # test case (left-left)
    rbtree = RedBlackTree()
    rbtree.insert(40)
    rbtree.insert(30)
    rbtree.insert(50)
    rbtree.insert(20)
    rbtree.insert(35)
    rbtree.remove(50)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 4
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 40
    assert rbtree.get_min() == 20
    assert rbtree.get_height() == 2
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 30
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 20
    assert rbtree._root.get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left() is None
    assert rbtree._root.get_left().get_right() is None

    assert rbtree._root.get_right().get_data() == 40
    assert rbtree._root.get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left().get_data() == 35
    assert rbtree._root.get_right().get_left().get_color() == Color.RED
    assert rbtree._root.get_right().get_left().get_left() is None
    assert rbtree._root.get_right().get_left().get_right() is None
    assert rbtree._root.get_right().get_right() is None


def test_double_black_left_right_case(helper):
    # test case (left-right)
    rbtree = RedBlackTree()
    rbtree.insert(40)
    rbtree.insert(30)
    rbtree.insert(50)
    rbtree.insert(35)
    rbtree.remove(50)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 3
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 40
    assert rbtree.get_min() == 30
    assert rbtree.get_height() == 1
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 35
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 30
    assert rbtree._root.get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left() is None
    assert rbtree._root.get_left().get_right() is None

    assert rbtree._root.get_right().get_data() == 40
    assert rbtree._root.get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left() is None
    assert rbtree._root.get_right().get_left() is None


def test_double_black_right_left_case(helper):
    # test case (right-left)
    rbtree = RedBlackTree()
    rbtree.insert(30)
    rbtree.insert(20)
    rbtree.insert(40)
    rbtree.insert(35)
    rbtree.remove(20)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 3
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 40
    assert rbtree.get_min() == 30
    assert rbtree.get_height() == 1
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 35
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 30
    assert rbtree._root.get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left() is None
    assert rbtree._root.get_left().get_right() is None

    assert rbtree._root.get_right().get_data() == 40
    assert rbtree._root.get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left() is None
    assert rbtree._root.get_right().get_left() is None


def test_double_black_right_right_case(helper):
    rbtree = RedBlackTree()
    rbtree.insert(30)
    rbtree.insert(20)
    rbtree.insert(40)
    rbtree.insert(50)
    rbtree.remove(20)
    # test tree characteristics
    assert helper.verify_bst_rules(rbtree._root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 3
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 50
    assert rbtree.get_min() == 30
    assert rbtree.get_height() == 1
    assert rbtree.get_depth() == 0
    assert rbtree.get_black_height() == 2
    # check data/colors
    assert isinstance(rbtree._root, RedBlackNode)
    assert rbtree._root.get_data() == 40
    assert rbtree._root.get_color() == Color.BLACK
    assert rbtree._root.get_left().get_data() == 30
    assert rbtree._root.get_left().get_color() == Color.BLACK
    assert rbtree._root.get_left().get_left() is None
    assert rbtree._root.get_left().get_right() is None

    assert rbtree._root.get_right().get_data() == 50
    assert rbtree._root.get_right().get_color() == Color.BLACK
    assert rbtree._root.get_right().get_left() is None
    assert rbtree._root.get_right().get_left() is None
