class Deque():
    """Basic object for the Deque data structure"""
    def __init__(self):
        self.container = []

    def __repr__(self):
        top_border = '─┬'
        middle = ' │'
        down_border = '─┴'
        for item in self.container:
            width = len(str(item))+2 #2: for a space before & after an item
            top_border += ('─'*width) + '┬'
            middle += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        top_border += '─'
        middle += ' '
        down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle, down_border)

    def __len__(self):
        return len(self.container)

    def add_left(self, item):
        """Insert value into the front of the Deque"""
        self.container.insert(0, item)

    def add_right(self, item):
        """Insert value into the end of the Deque"""
        self.container.append(item)

    def remove_left(self):
        """Removes value from the Deque (first-inserted item)"""
        return self.container.pop(0)

    def remove_right(self):
        """Removes value from the Deque (most recent)"""
        return self.container.pop()

    def peek(self):
        """Returns the Deque recent item"""
        return self.container[-1]

    def is_empty(self):
        """Checks if the Deque is empty"""
        return len(self) == 0

    def clear(self):
        """Clears the whole Deque"""
        self.container = []

    def rotate(self, k):
        """Circularly shift rightward by k steps"""
        pass




if __name__ == "__main__":
    q = Deque()
    q.add_front(0) #0
    q.add_end(1)   #0 1
    q.add_end(8)   #0 1 8
    q.add_front(9) #9 0 1 8
    print(q)
    