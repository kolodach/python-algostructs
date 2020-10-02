from arraylist import ArrayList

def test__init__CreatesDefaultCapacity():
    list = ArrayList()
    assert len(list._items) == ArrayList.INITAL_CAPACITY
