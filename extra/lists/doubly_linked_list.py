"""
A doubly linked list is a simple linear data structure where objects are linked
using pointers to their associated location. Unlike arrays whose objects are
stored at continuous locations. Each node stores two references: the first is a
reference to the next element of the sequence. And the second is a reference to
the previous element of the sequence.

The first node of a doubly linked list is known as the **head** of the doubly
linked list. By starting at the doubly linked list's head and moving to the
latter nodes using each node's next reference, we can reach the end of the list.
This process is commonly known as *traversing* the doubly linked list. 
 
[image]

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **m** is the number of elements in the *other* container.
- **k** is the value of a parameter.

+----------------+--------------------------------------------------------+-------------+-------------+
| Method         | Description                                            | Worst-case  | Optimal     |
+================+========================================================+=============+=============+
| __len__()      | Returns the number of nodes                            | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| is_empty()     | Checks if object is empty                              | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __repr__()     | Represents the object                                  | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __iters__()    | Iterates over the object                               | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __eq__()       | Checks if two linked lists are equal                   | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __ne__()       | Checks if two linked lists are not equal               | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __lt__()       | Checks if the linked list is less than the other       | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __le__()       | Checks if the list is less than or equal the other     | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __gt__()       | Checks if the linked list is greater than the other    | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __gt__()       | Checks if the list is greater than or equal the other  | O(min(n,m)) | O(min(n,m)) |
+----------------+--------------------------------------------------------+-------------+-------------+
| __contains__() | Checks the existence of the given item                 | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| __getitem__()  | Returns the element at a certain index.                |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| add_front()    | Adds the given item at the head                        | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| add_end()      | Adds the given item at the tail                        | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| insert()       | Adds the given item at the given index                 |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| __setitem__()  | Replaces the value at the given index with given value |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| __delitem__()  | Deletes the value at the given index                   |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_front() | Removes the node at the head                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove_end()   | Removes the node at the tail                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| remove()       | Removes the given value if found                       | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| clear()        | Clears the whole linked list                           | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| split()        | Splits the list into two at the given index            |O(min(k,n/2))|O(min(k,n/2))|
+----------------+--------------------------------------------------------+-------------+-------------+
| extend()       | Extends the linked list using another linked list.     | O(1)        | O(1)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| rotate_left()  | Left-rotates the list by the given value               | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| rotate_right() | Right-rotates the list by the given value              | O(k)        | O(k)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| reverse()      | Reverses the linked list                               | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| to_list()      | Converts the linked list to built-in list              | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| count()        | Counts how many the given value found in the list      | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+
| copy()         | Copies the linked list                                 | O(n)        | O(n)        |
+----------------+--------------------------------------------------------+-------------+-------------+


Class Documentation
===================
Here are all of the public methods that can be used with `Doubly Linked List()`
objects:
"""
from extra.lists.linked_list import Node, LinkedList




class DoublyNode(Node):
    """Basic object for the Node used for doubly linked lists"""
    __name__ = "extra.DoublyNode()"


    def __init__(self, item):
        """
        Creates a `DoublyNode()` object used mainly with DoublyLinkedList()
        objects!!

        Parameters
        ----------
        item: object 
            The value to be saved within the `DoublyNode()` instance.

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        ValueError: If the given item is `None`.
        """
        super().__init__(item)
        self._prev = None


    def __repr__(self):
        """
        Represents `DoublyNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `Node()` instance.
        
        Example
        -------
        >>> x = Node(10)
        >>> x
        >>> Node(data: 10, next:None)
        """
        prv = self._prev.get_data() if self._prev is not None else None
        nxt = self._next.get_data() if self._next is not None else None
        return f"DoublyNode(data: {self._data}, prev: {prv}, next: {nxt})"
    

    def get_prev(self):
        """
        Returns the prev `DoublyNode()` instance of the current one.

        Returns
        -------
        Node():
            The `Node()` instance that follows the current `DoublyNode()` or
            `None`.
        """
        return self._prev
    

    def set_prev(self, prev_node):
        """
        Sets the prev pointer of the current `DoublyNode()` to the given node.

        Parameters
        ----------
        next_node: DoublyNode()
            The `DoublyNode()` instance that will follow the current one.

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        """
        if prev_node is None:
            self._prev = None
        elif not isinstance(prev_node, DoublyNode):
            raise TypeError(
                f"Can't set {type(prev_node)} as a {self.__name__}!!")
        else:
            self._prev = prev_node
            prev_node._next = self
    

    def set_next(self, next_node):
        """
        Sets the next pointer of the current `DoublyNode()` to the given node.

        Parameters
        ----------
        next_node: DoublyNode()
            The `DoublyNode()` that will follow the current one.

        Raises
        ------
        TypeError: If the given item is an `Extra` object.
        """
        if next_node is None:
            self._next = None
        elif not isinstance(next_node, DoublyNode):
            raise TypeError(
                f"Can't set {type(next_node)} as a {self.__name__}!!")
        else:
            self._next = next_node
            next_node._prev = self




class DoublyLinkedList(LinkedList):
    """Basic object for the double linked list"""
    _basic_node = DoublyNode
    __name__ = "extra.DoublyLinkedList()"
   
   
    def __init__(self):
        """
        Creates a DoublyLinkedList() object!!
        
        Example
        -------
        >>> ll = DoublyLinkedList()
        >>> type(ll)
        <class 'extra.lists.doubly_linked_list.DoublyLinkedList'>
        """
        super().__init__()
        self._tail = None
    

    def _create_instance(self):
        """
        Returns an instance of the class

        Returns
        -------
        DoublyLinkedList()
            It returns an empty DoublyLinkedList() instance.
        """
        return DoublyLinkedList()


    @classmethod
    def from_iterable(cls, iterable):
        """
        A class method which creates a doubly linked list instance using an
        iterable in time-complexity of O(n) where **n** is the number of
        elements inside the given `iterable`.

        Parameters
        ----------
        iterable: iterable object.
            An iterable python object that implements the `__iter__` method.
            For example, `list` and `tuple` are both iterables.
        
        Returns
        -------
        DoublyLinkedList()
            It returns a DoublyLinkedList() instance with the same values in
            the same order.
        
        Raises
        ------
        TypeError: It can be raised in two cases
            1. In case the given object isn't iterable.
            2. If one of the iterable elements is an `Extra` object.

        ValueError: If one of the iterable elements is `None`.

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([10, -5, 7, 9])
        >>> dll
         ┌────┐ ┌────┐ ┌───┐ ┌───┐ 
        ⟷│ 10 │⟷│ -5 │⟷│ 7 │⟷│ 9 │⟷
         └────┘ └────┘ └───┘ └───┘ 

        Using an iterable object with `None` as one of its elements will raise
        `ValueError`

        >>> dll = DoublyLinkedList.from_iterable([2, None])
        ValueError: Can't use `None` as an element within `extra.DoublyLinkedList()`!!
        
        Using a non-iterable object will raise `TypeError`

        >>> dll = DoublyLinkedList.from_iterable(2)
        TypeError: The given object isn't iterable!!
        
        Using nested `DoublyLinkedList` objects will raise `TypeError` as well

        >>> dll_1 = DoublyLinkedList.from_iterable([1])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, dll_1])
        TypeError: Can't create `extra.DoublyLinkedList()` using `extra.DoublyLinkedList()`!!

        Note
        -----
        Since most of the data structures found in this package are iterables, 
        then you can use this classmethod to convert from one data structure to
        `DoublyLinkedList` just like so:

        >>> ll = LinkedList.from_iterable([2, 5])
        >>> dll = DoublyLinkedList.from_iterable(ll)
        >>> dll
         ┌───┐ ┌───┐ 
        ⟷│ 2 │⟷│ 5 │⟷
         └───┘ └───┘ 
        """
        return super().from_iterable(iterable)
    

    ##############################      PRINT     ##############################
    def _print_node(self, node):
        """
        Prints the given node of the DoublyLinkedList() instance.

        Parameters
        ----------
        node: `DoublyNode()`
            The `DoublyNode()` object that we want to print.

        Returns
        -------
        tuple
            It returns a tuple of three strings representing the given node
            when printed.
        
        Raises
        ------
        AssertionError: In case the given object isn't `DoublyNode()`

        Example
        -------
        >>> dll = DoublyLinkedList()
        >>> dll.add_front(10)
        >>> lines = ["".join(x) for x in dll._print_node(dll._head)]
        >>> "\n".join(lines)
         ┌────┐
        ⟷│ 10 │⟷
         └────┘
        """
        top_border    = [' ┌']
        middle_border = ['⟷│']
        lower_border  = [' └']
        item = node._represent()
        width = len(item)+2 #2: for a space before & after an item
        top_border += (['─']*width) + ['┐']
        middle_border += [f" {item} │"]
        lower_border += (['─']*width) + ['┘']
        if node.get_next() is None:
            top_border += [' ']
            middle_border += ['⟷']
            lower_border += [' ']
        return top_border, middle_border, lower_border


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the DoublyLinkedList() in time-complexity of O(1)
        
        Returns
        -------
        int:
            The length of the DoublyLinkedList() instance. By Length, I mean
            the number of nodes of in the instance.
        
        Examples
        --------
        >>> dll = DoublyLinkedList()
        >>> len(dll)
        0
        >>> dll = DoublyLinkedList.from_iterable((2, 5, 0))
        >>> len(dll)
        3
        """
        return self._length
    

    def is_empty(self):
        """
        Checks if DoublyLinkedList() instance is empty or not in time-
        complexity of O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the DoublyLinkedList() instance is empty
            or not. `True` shows that this instance is empty and `False` shows
            it's not empty.
        
        Example
        --------
        >>> dll = DoublyLinkedList()
        >>> dll.is_empty()
        True
        >>> dll.add_front(5)
        >>> dll.is_empty()
        False
        """
        return self._length == 0

    
    ##############################    OPERATOR    ##############################
    def __iter__(self):
        """
        Iterates over the DoublyLinkedList() instance and returns a generator
        in time-complexity of O(n) where **n** is the number of elements in the 
        DoublyLinkedList() instance.

        Returns
        -------
        generator:
            The value of each node in the instance.
        
        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> for item in dll:
        ...     print(item)
        1
        2
        3
        """
        return super().__iter__()
    

    def __eq__(self, other):
        """
        Checks if two DoublyLinkedList() instances are equal to each other.
        And this happens if, and only if, the following two conditions are met:
        
        1. The two instances are equal in length (have same number of elements).

        2. Every single element in the first instance is equal, in both \
            **value** and **type**, to the opposing element of the other \
            instance.

        Parameters
        ----------
        other: DoublyLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if both instances are equal, and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a DoublyLinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------
        >>> dll_1 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 2])
        >>> dll_1 == dll_2
        False
        >>> dll_1 == dll_1
        True
        """
        return super().__eq__(other)


    def __ne__(self, other):
        """
        Checks if two DoublyLinkedList() instances are NOT equal to each other.
        And this happens if, and only if, either one of the following two
        conditions is satisfied:
        
        1. The two instances are NOT equal in length (number of elements).

        2. Just one element in the first instance is NOT equal, in either \
            **value** or **type**, to the opposing element of the other \
            instance.

        Parameters
        ----------
        other: DoublyLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if both instances are NOT equal, and `False` otherwise.

        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of  the opposing element in the other instance.
        
        Examples
        --------
        >>> dll_1 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 2])
        >>> dll_1 != dll_2
        True
        >>> dll_1 != dll_1
        False
        """
        return super().__ne__(other)
    

    def __le__(self, other):
        """
        Checks if the first DoublyLinkedList() instance is less than or equal to
        the other instance. And this happens if all elements in the first
        instance are equal or less than the opposing elements of the second
        instance.

        Parameters
        ----------
        DoublyLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is less than or equal to the second
            instance, and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 3, 2])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 <= dll_2
        True

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 3])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 <= dll_2
        True

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 5])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 <= dll_2
        False

        >>> dll_1 = DoublyLinkedList.from_iterable([5, 2, 1])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 <= dll_2
        False

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_1 <= dll_2
        True
        """
        return super().__le__(other)
    
    
    def __gt__(self, other):
        """
        Checks if the first DoublyLinkedList() instance is greater than the
        other instance. And this happens if all elements in the first instance
        are equal with at least one element greater than the opposing element of
        the second instance.

        Parameters
        ----------
        DoublyLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is greater than the second, and `False`
            otherwise.

        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.
        
        Examples
        --------

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 3, 5])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 > dll_2
        True

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 3, 2, 1])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 2])
        >>> dll_1 > dll_2
        True

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 5])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 > dll_2
        False

        >>> dll_1 = DoublyLinkedList.from_iterable([5, 2, 1])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 > dll_2
        False

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_1 > dll_2
        False
        """
        return super().__gt__(other)
    

    def __ge__(self, other):
        """
        Checks if the first DoublyLinkedList() instance is greater than or equal
        to the other instance. And this happens if all elements in the first
        instance are greater than or equal to the opposing element of the
        second instance.

        Parameters
        ----------
        DoublyLinkedList()
            The other instance that we want to compare with the current one
        
        Returns
        -------
        bool
            `True` if the first instance is greater than or equal to the second,
            and `False` otherwise.
        
        Raises
        ------
        TypeError: This happens in two cases
            1. If the other instance isn't a LinkedList() instance.
            2. In case one element in the first instance doesn't match the \
                type of the opposing element in the other instance.

        Examples
        --------

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 3, 5])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 >= dll_2
        True

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 3, 2, 1])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 2])
        >>> dll_1 >= dll_2
        True

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 5])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 >= dll_2
        False

        >>> dll_1 = DoublyLinkedList.from_iterable([5, 2, 1])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 3, 3])
        >>> dll_1 >= dll_2
        False

        >>> dll_1 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_2 = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll_1 >= dll_2
        True
        """
        return super().__ge__(other)


    ##############################     SEARCH     ##############################
    def __contains__(self, value):
        """
        Checks if the given value exists in the DoublyLinkedList() instance in
        time-complexity of O(n) where **n** is the total number of elements in
        the DoublyLinkedList() instance.

        Parameters
        ----------
        value: Object
            The value to be searched for in the DoublyLinkedList() instance.
        
        Returns
        -------
        bool
            `True` if the given value exists in the DoublyLinkedList() instance,
            and `False` otherwise.

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 3, 5])
        >>> 1 in dll
        True
        >>> 0 in dll
        False
        >>> "hello" in dll
        False
        """
        return super().__contains__(value)


    def _get_node(self, idx):
        """
        Iterates over the DoublyLinkedList() instance and returns the node at
        the given index. If the given index is less than half of the
        DoublyLinkedList() length, it starts iterating from left to right. And
        if the index is bigger, it starts iterating from right to left in order
        to make the searching process a little bit faster.

        Parameters
        ----------
        idx: int
            An integer number pointing at the node to be returned.
        
        Returns
        -------
        DoublyNode():
            The previus `DoublyNode()` object to the node at the given index.
        DoublyNode():
            The `DoublyNode()` object at the given index.
        
        Raises
        ------
        AssertionError: If the given index is bigger than the LinkedList length.
        
        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> prev_node, node = dll._get_node(2)
        >>> prev_node
        (DoublyNode(data: 2, prev: 1, next: 3)
        >>> node
        DoublyNode(data: 3, prev: 2, next: None)
        """
        # iterate over the double linked list (forwards)
        if idx <= self._length//2:
            return super()._get_node(idx)
        else:
            # iterate over the double linked list (backwards)
            counter = self._length
            curr_node = self._tail
            while(counter > idx):
                counter -= 1
                curr_node = curr_node.get_prev()
            prev_node = curr_node
            curr_node = prev_node.get_next()
            return prev_node, curr_node


    def __getitem__(self, idx):
        """
        Retrieves the element at the given index. The given index could be a 
        zero-based `int` or a `slice` object. This method supports negative
        indexing. This method does that in time-complexity of O(k) where **k**
        is the given index.

        Parameters
        ----------
        idx: int or slice
            The index (multiple indices) to be used to retrieve values from the
            LinkedList() instance.
        
        Returns
        -------
        object or DoublyLinkedList():
            If the given index is an `int`, then it returns the value at this 
            index. If the given index is a `slice` object, then it returns a 
            DoublyLinkedList() instance containing the desired values.
        
        Raises
        ------
        TypeError: If the given index isn't `int`.
        IndexError: If the given index is out of the DoublyLinkedList()
            boundaries.

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3, 4, 5])
        >>> dll[0]
        1
        >>> dll[-2]
        4
        >>> dll[2:]
         ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 3 │⟷│ 4 │⟷│ 5 │⟷
         └───┘ └───┘ └───┘ 
        >>> dll[0:5:2]
         ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 3 │⟷│ 5 │⟷
         └───┘ └───┘ └───┘ 
        >>> dll[10]
        IndexError: Given index is out of the boundaries!!
        """
        return super().__getitem__(idx)
    

    ##############################     INSERT     ##############################
    def _insert_node(self, prev_node, item):
        """
        Inserts a `new_node` at a position defined by the given `prev_node`.

        Parameters
        ----------
        prev_node: DoublyNode()
            A reference to the node next to which a new node should be inserted.
        new_node: DoublyNode()
            A referece to the new node to be inserted.
        
        Returns
        -------
        DoublyNode():
            A reference to the new node after being inserted in the
            DoublyLinkedList().
            
        Raises
        ------
        AssertionError: This happens in one of the following cases:
            1. The `prev_node` isn't a `DoublyNode()` object
            2. The `new_node` isn't a `DoublyNode()` object
        
        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> new_node = DoublyNode(10)
        >>> dll._insert_node(dll._head, new_node)
        DoublyNode(data: 10, prev: 1, next: 2)
        """
        # handle different types of `item`
        if isinstance(item, self._basic_node):
            assert item.get_data() is not None, \
                "Can't insert `None` value as a node!!"
            new_node = item
        else:
            assert item is not None, "Can't insert `None` value as a node!!"
            new_node = self._basic_node(item)
        # start inserting the node
        if self._length == 0:
            self._head = self._tail = new_node
        elif self._length == 1:
            if prev_node is None:
                new_node.set_next(self._tail)
                self._head = new_node
            else:
                self._tail = new_node
                self._head.set_next(self._tail)
        else:
            if prev_node is None:
                new_node.set_next(self._head)
                self._head = new_node
            else:
                if prev_node.get_next() is None:
                    self._tail.set_next(new_node)
                    self._tail = new_node
                else:
                    new_node.set_next(prev_node.get_next())
                    prev_node.set_next(new_node)
        self._length += 1
        return new_node
    

    def add_front(self, item):
        """
        Adds the given value at the head of the DoublyLinkedList() instance in
        time-complexity of O(1).

        Parameters
        ----------
        item: object
            The value to be inserted at the DoublyLinkedList() head.
        
        Raises
        ------
        TypeError: If the given item is an instance of `Extra`.
        ValueError: If the given item is `None`.

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll.add_front(10)
        >>> dll
         ┌────┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 10 │⟷│ 1 │⟷│ 2 │⟷│ 3 │⟷
         └────┘ └───┘ └───┘ └───┘ 
        """
        super().add_front(item)


    def add_end(self, item):
        """
        Adds the given value at the tail of the DoublyLinkedList() instance in
        time-complexity of O(1).

        Parameters
        ----------
        item: object
            The value to be inserted at the DoublyLinkedList() tail.
        
        Raises
        ------
        TypeError: If the given item is an instance of `Extra`.
        ValueError: If the given item is `None`.

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll.add_end(10)
        >>> dll
         ┌───┐ ┌───┐ ┌───┐ ┌────┐ 
        ⟷│ 1 │⟷│ 2 │⟷│ 3 │⟷│ 10 │⟷
         └───┘ └───┘ └───┘ └────┘         
        """
        super().add_end(item)
    

    def insert(self, idx, item):
        """
        Insertd a value at a position defined by the given index.

        Parameters
        ----------
        idx: int
            An integer pointing to the index at which the given value should be
            inserted.
        item: object
            An object to be inserted.
              
        Raises
        ------
        IndexError: This happens in one of the following cases: 
            1. If the given index is out of the DoublyLinkedList() boundaries.
            2. If the given index is less than zero (-ve).
        TypeError: This happens in one of the following cases:
            1. If the given index isn't integer.
            2. If the given item is an instance of `Extra`.
        ValueError: If the given item is `None`.
        
        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll.insert(1, 10)
        >>> dll
         ┌───┐ ┌────┐ ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 10 │⟷│ 2 │⟷│ 3 │⟷
         └───┘ └────┘ └───┘ └───┘ 
        >>> dll.insert(5, 8)
        IndexError: Given index is out of the boundaries!!
        >>> dll.insert(1, None)
        ValueError: Can't use `None` as an element within `extra.DoublyLinkedList()`!!
        >>> dll.insert(-1, 100)
        IndexError: Negative indexing isn't supported with this functinoality!!
        """
        super().insert(idx, item)
    

    def extend(self, other):
        """
        Extends the current DoublyLinkedList() instance by appending the
        elements of the other DoublyLinkedList() instance in time-complexity of
        O(1).

        Parameters
        ----------
        other: DoublyLinkedList()
            The DoublyLinkedList() instance whose elements will be appended.
                
        Raises
        ------
        TypeError: If the given object isn't a DoublyLinkedList() instance.

        Example
        -------
        >>> dll_1 = DoublyLinkedList.from_iterable([1, 2])
        >>> dll_2 = DoublyLinkedList.from_iterable([3, 4, 5])
        >>> dll_1.extend(dll_2)
        >>> dll_1
         ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 2 │⟷│ 3 │⟷│ 4 │⟷│ 5 │⟷
         └───┘ └───┘ └───┘ └───┘ └───┘ 
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Type Mismatch! " + 
                f"Can't extend `{self.__name__}` with `{type(other)}`!!"
            )
        if other.is_empty():
            pass # do nothing
        elif self.is_empty(): 
            self._head = other._head
            self._tail = other._tail
            self._length += other._length
        else:
            self._tail.set_next(other._head)
            self._tail = other._tail
            self._length += other._length


    ##############################       SET      ##############################
    def __setitem__(self, idx, item):
        """
        Replaces the value at the given index with the given item. It does that
        in time-complexity of O(min(k,n/2)) where **k** is the index value and
        **n** is the number of elements in the DoublyLinkedList() instance.

        Parameters
        ----------
        idx: int
            An integer pointing to the index at which the given value should be
            inserted.
        item: object
            An object to be inserted.
        
        Raises
        ------
        IndexError: If the given index is either negative or out of the
            boundaries.
        ValueError: If the given object is `None`.
        TypeError: This get raised in one of the following cases:
            1. If the given index type is not `int`.
            2. If the given object is an instance of `Extra`.
        
        TODOs
        -----
        1. Handle negative indexing
        2. Handle slice objects

        Examples
        --------
        >>> ll = LinkedList.from_iterable([1, 2, 3])
        >>> ll[0] = 10
        >>> ll[2] = 30
        >>> ll
        ┌────┐ ┌───┐ ┌────┐ 
        │ 10 │⟷│ 2 │⟷│ 30 │⟷
        └────┘ └───┘ └────┘ 
        >>> ll[-1] = 0
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> ll[3] = 40
        IndexError: Given index is out of the boundaries!!
        """
        super().__setitem__(idx, item)


    ##############################     REMOVE     ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        """
        Removes a node from the DoublyLinkedList() instance.

        Parameters
        ----------
        prev_node: DoublyNode()
            A reference to the node next to the node that will be removed.
        node_to_be_removed: DoublyNode()
            A referece to the node to be removed.
        
        Raises
        ------
        AssertionError: This happens in one of the following cases:
            1. The `prev_node` isn't a `DoublyNode()` object or `None.
            2. The `node_to_be_removed` isn't a `DoublyNode()` object
        
        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll
         ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 2 │⟷│ 3 │⟷
         └───┘ └───┘ └───┘ 
        >>> dll._remove_node(dll._head, dll._head._next)
        >>> dll
         ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 3 │⟷
         └───┘ └───┘ 
        """
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert node_to_be_removed is not None, "Can't remove `None`!!"

        next_node = node_to_be_removed.get_next()
        # if node to be removed is the first
        if self._length == 1:
            #NOTE: don't use set_data() here
            self._head.data = self._tail.data = None
            self._length -= 1
        elif self._length == 2:
            if prev_node is None:
                next_node.set_prev(None)
                self._head = next_node
            elif next_node is None:
                prev_node.set_next(None)
                self._tail = prev_node
            self._length -= 1
        else:
            if next_node is None:
                prev_node.set_next(next_node)
                self._tail = prev_node
                self._length -= 1
            else:
                super()._remove_node(prev_node, node_to_be_removed)


    def __delitem__(self, idx):
        """
        Deletes the value at the given index. It does that in time-complexity
        of O(min(k,n/2)) where **k** is the index value and **n** is the number
        of elements in the DoublyLinkedList() instance.

        Parameters
        ----------
        idx: int
            An integer pointing to the index where the node that should be
            removed.
        
        Raises
        ------
        IndexError: If the given index is either negative or out of the
            boundaries.
        
        TODOs
        -----
        1. Handle negative indexing
        2. Handle slice objects

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> del dll[0]
        >>> dll
         ┌───┐ ┌───┐ 
        ⟷│ 2 │⟷│ 3 │⟷
         └───┘ └───┘ 
        >>> del dll[-1]
        IndexError: Negative indexing isn't supported with this functinoality!!
        >>> del dll[3]
        IndexError: Given index is out of the boundaries!!
        """
        super().__delitem__(idx)


    def remove_front(self):
        """
        Removes the value at the head of the DoublyLinkedList() instance in time-
        complexity of O(1).

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll.remove_front()
        >>> dll
         ┌───┐ ┌───┐ 
        ⟷│ 2 │⟷│ 3 │⟷
         └───┘ └───┘ 
        >>> dll.remove_front()
        >>> dll
         ┌───┐ 
        ⟷│ 3 │⟷
         └───┘ 
        """
        super().remove_front()
    

    def remove_end(self):
        """
        Removes the value at the tail of the DoublyLinkedList() instance in
        time-complexity of O(1).

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll.remove_end()
        >>> dll
         ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 2 │⟷
         └───┘ └───┘ 
        >>> dll.remove_end()
        >>> dll
         ┌───┐ 
        ⟷│ 1 │⟷
         └───┘ 
        """
        super().remove_end()
    

    def remove(self, value, all=True):
        """
        Removes node(s) whose value equal to the given value.

        Parameters
        ----------
        value: object
            The value to be removed from the DoublyLinkedList() instance.
        all: bool
            A flag (default: `True`); if `True`, all occurrences of the given
            value are remove. If `False`, only the first occurrence is removed.
        
        Raises
        ------
        ValueError: If The given value is `None`.
        TypeError: This get raised in one of the following cases:
            1. If the type of the `all` flag isn't boolean.
            2. If the given value is an instance of `Extra` class.
        
        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3, 2, 2])
        >>> dll.remove(2, False)
        >>> dll
         ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 3 │⟷│ 2 │⟷│ 2 │⟷
         └───┘ └───┘ └───┘ └───┘ 
        >>> dll._remove_value(10) #does nothing
        >>> dll._remove_value(2, True)
        >>> dll
         ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 3 │⟷
         └───┘ └───┘ 
        """
        super().remove(value, all)    
    

    def clear(self):
        """
        Removes all nodes within the DoublyLinkedList() in time-complexity of
        O(1).

        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
         ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 2 │⟷│ 3 │⟷
         └───┘ └───┘ └───┘ 
        >>> dll.clear()
        >>> dll.is_empty()
        True
        >>> dll
        ┌─
        │
        └─
        """
        super().clear()
    

    ##############################      SPLIT      ##############################
    def split(self, idx):
        """
        Splits the DoublyLinkedList() instance into two instances based on the
        given index in time-complexity of O(min(k,n/2)) where **k** is the index
        and **n** is the number of elements in the original instance. We can
        consider `idx` as the start index of the second DoublyLinkedList() after
        splitting. If `idx=0`, then the first returned DoublyLinkedList() will
        be empty while the second returned DoublyLinkedList() will be the same
        length as the original.

        Parameters
        ----------
        idx: int
            A positive integer pointing to the index at which the 
            DoublyLinkedList() instance should be split.
        
        Returns
        -------
        DoublyLinkedList(): 
            The left DoublyLinkedList() instance returned after split.
        DoublyLinkedList(): 
            The right DoublyLinkedList() instance returned after split
        
        Raises
        ------
        TypeError: If the given index isn't `int`.
        IndexError: If the given index is either negative or out of the
            DoublyLinkedList() boundaries.

        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3])
        >>> dll
         ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 1 │⟷│ 2 │⟷│ 3 │⟷
         └───┘ └───┘ └───┘ 
        >>> left, right = dll._split(1)
        >>> left
         ┌───┐ 
        ⟷│ 1 │⟷
         └───┘ 
        >>> right
         ┌───┐ ┌───┐ 
        ⟷│ 2 │⟷│ 3 │⟷
         └───┘ └───┘ 
        """
        return super().split(idx)
    

    ##############################    ROTATION    ##############################
    def rotate_left(self, distance, inplace=True):
        """
        Rotates the DoublyLinkedList() instance to the left by a certain given
        `distance`. If `inplace=True`, it does the rotation in-place. If not, 
        it returns the rotated instance. The time-compelxity of this method is
        of O(min(k,n/2)) where **k** is the index and  **n** is the number of
        elements in the DoublyLinkedList() instance.

        Parameters
        ----------
        distance: int
            The rotation distance to the left.
        inplace: bool
            A flag to determine if the rotation is going to be in-place or not.
            (default `True`).
        
        Returns
        -------
        DoublyLinkedList():
            The rotated instance if `inplace=True`
        
        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3, 4])
        >>> dll.rotate_left(1)
         ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 2 │⟷│ 3 │⟷│ 4 │⟷│ 1 │⟷
         └───┘ └───┘ └───┘ └───┘ 
        >>> # it works fine when the distance is bigger than the instance length
        >>> dll.rotate_left(10)
         ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 3 │⟷│ 4 │⟷│ 1 │⟷│ 2 │⟷
         └───┘ └───┘ └───┘ └───┘ 
        """
        if type(inplace) != bool:
            raise TypeError("`inplace` is a boolean flag (True by default)!!")
        super()._validate_distance(distance)
        rotated = self._rotate(distance, "LEFT")
        if not inplace: return rotated
        self._head = rotated._head
        self._tail = rotated._tail
        
    
    def rotate_right(self, distance, inplace=True):
        """
        Rotates the DoublyLinkedList() instance to the right by a certain given
        `distance`. If `inplace=True`, it does the rotation in-place. If not, 
        it returns the rotated instance. The time-compelxity of this method is
        O(min(k,n/2)) where **k** is the index and **n** is the number of
        elements in the original instance.

        Parameters
        ----------
        distance: int
            The rotation distance to the right.
        inplace: bool
            A flag to determine if the rotation is going to be in-place or not.
            (default `True`).
        
        Returns
        -------
        DoublyLinkedList():
            The rotated instance if `inplace=True`
        
        Examples
        --------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3, 4])
        >>> dll.rotate_right(1)
         ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 4 │⟷│ 1 │⟷│ 2 │⟷│ 3 │⟷
         └───┘ └───┘ └───┘ └───┘ 
        >>> # it works fine when the distance is bigger than the instance length
        >>> dll.rotate_right(15)
         ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 2 │⟷│ 3 │⟷│ 4 │⟷│ 1 │⟷
         └───┘ └───┘ └───┘ └───┘ 
        """
        if type(inplace) != bool:
            raise TypeError("`inplace` is a boolean flag (True by default)!!")
        super()._validate_distance(distance)
        rotated = self._rotate(distance, "RIGHT")
        if not inplace: return rotated
        self._head = rotated._head
        self._tail = rotated._tail


    ##############################      MISC      ##############################
    def reverse(self):
        """
        Reverses the whole DoublyLinkedList() instance in time-complexity of
        O(n) where **n** is the number of elements in the DoublyLinkedList().

        Returns
        -------
        DoublyLinkedList():
            The reversed DoublyLinkedList() instance.
        
        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([1, 2, 3, 4])
        >>> dll.reverse()
         ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        ⟷│ 4 │⟷│ 3 │⟷│ 2 │⟷│ 1 │⟷
         └───┘ └───┘ └───┘ └───┘ 
        """
        return super().reverse()
    

    def to_list(self):
        """
        Converts the DoublyLinkedList() instance to a `list` in time-complexity
        of O(n) where **n** is the number of elements in the instance.

        Returns
        -------
        list:
            A `list` object containing the same elements as the
            DoublyLinkedList() instance.
        
        Example
        -------
        >>> dll = DoublyLinkedList()
        >>> dll.add_front(20)
        >>> dll.add_front(10)
        >>> dll.add_end(30)
        >>> dll
         ┌────┐ ┌────┐ ┌────┐ 
        ⟷│ 10 │⟷│ 20 │⟷│ 30 │⟷
         └────┘ └────┘ └────┘ 
        >>> dll.to_list()
        [10, 20, 30]
        """
        return super().to_list()
    

    def count(self, value):
        """
        Counts the number of occurrence the given value is in our
        DoublyLinkedList() instance.

        Parameters
        ----------
        value: object
            The object to count its occurrences
        
        Returns
        -------
        int:
            The number of times the given value is found in the
            DoublyLinkedList() instance. And 0 if it wasn't found.
        
        Example
        -------
        >>> dll = DoublyLinkedList.from_iterable([0, 1, 1, 2, 3, 5])
        >>> dll.count(3)
        1
        >>> dll.count(1)
        2
        >>> dll.count("he")
        0
        """
        return super().count(value)
    

