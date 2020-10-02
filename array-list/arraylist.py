"""
Array list is used as a dynamic array. It doubles it's size each time when the
current capacity is filled.
"""
class ArrayList:
    INITAL_CAPACITY = 1

    def __init__(self, capacity = INITAL_CAPACITY):
        self._items = tuple(0 for i in range(capacity))
        self._length = 0
