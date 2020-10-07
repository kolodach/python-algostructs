import pytest # pylint: disable=import-error
from linkedlist import LinkedList, Node

# Node

def test_Node_shouldCreateNodeWithDefaultArgs():
    # act
    sut = Node()

    # assert
    assert sut.value == None
    assert sut.next == None

def test_Node_shouldCreateNodeWithActualArgs():
    # arrange
    value = 1
    next_node = Node()

    # act
    sut = Node(value, next_node)

    # assert
    assert sut.value == value
    assert sut.next == next_node

def test_str_ShouldCreateExpectedString():
    # arrange
    next_node = Node(1)
    node = Node(2, next_node)

    # act
    node_str = format(node)
    next_node_str = format(next_node)

    # assert
    assert node_str == "Node(value = 2, next = Node)"
    assert next_node_str == "Node(value = 1, next = None)"

# Linked List

def test_LinkedList_ShouldCreateEmptyInstance():
    # act
    sut = LinkedList()

    # assert
    sut.head = None
    sut._length = 0

def test_len_ShouldReturnCorrectLength():
    # arrange
    sut = LinkedList()
    sut.add_last(1)

    # act
    length = len(sut)

    # assert
    assert length == 1

def test_LinkedList_firstShouldInsertFirst():
    # arrange
    items = ["a", 1, None, True]
    sut = LinkedList()

    # act
    sut.add_first(items[0])
    sut.add_first(items[1])
    sut.add_first(items[2])
    sut.add_first(items[3])

    # assert
    assert sut.head.value == items[3]
    assert sut.head.next.value == items[2]
    assert sut.head.next.next.value == items[1]
    assert sut.head.next.next.next.value == items[0]
    assert sut.head.next.next.next.next == None
    assert sut.tail.value == items[0]
    assert sut._length == 4

def test_LinkedList_lastShouldInsertLast():
    # arrange
    items = ["a", 1, None, True]
    sut = LinkedList()

    # act
    sut.add_last(items[0])
    sut.add_last(items[1])
    sut.add_last(items[2])
    sut.add_last(items[3])

    # assert
    assert sut.head.value == items[0]
    assert sut.head.next.value == items[1]
    assert sut.head.next.next.value == items[2]
    assert sut.head.next.next.next.value == items[3]
    assert sut.head.next.next.next.next == None
    assert sut.tail.value == items[3]
    assert sut._length == 4


def test_add_at_ShouldInstertElementInTheMiddle():
    # arrange
    sut = LinkedList()
    sut.add_last(1)
    sut.add_last(3)

    # act
    sut.add_at(2, 1)

    # assert
    assert sut.head.value == 1
    assert sut.head.next.value == 2
    assert sut.tail.value == 3
    assert sut._length == 3

def test_add_at_ShouldInsertFirstElement():
    # arrange
    sut = LinkedList()
    sut.add_last(1)

    # act
    sut.add_at(0, 0)

    # assert
    assert sut.head.value == 0
    assert sut.head.next.value == 1
    assert sut.tail.value == 1
    assert sut._length == 2

def test_add_at_ShouldInsertLastElement():
    # arrange
    sut = LinkedList()
    sut.add_last(1)

    # act
    sut.add_at(2, 1)

    # assert
    assert sut.head.value == 1
    assert sut.head.next.value == 2
    assert sut.tail.value == 2
    assert sut._length == 2

def test_add_at_ShouldInsertSingleElement():
    # arrange
    sut = LinkedList()

    # act
    sut.add_at(1, 0)

    # assert
    assert sut.head.value == 1
    assert sut.head.next== None
    assert sut.tail.value == 1
    assert sut._length == 1

def test_add_at_ShouldRaiseForInvalidIndex():
    # arrage
    sut = LinkedList()

    # act, assert
    with pytest.raises(IndexError):
        sut.add_at(1, 1)

def test_LinkedList_firstSouldReturNoneIfEmpty():
    # arrange
    sut = LinkedList()
    expected = None

    # act
    received = sut.first()

    # assert
    assert expected == received

def test_LinkedList_firstShouldReturnCorrectValue():
    # arrange
    sut = LinkedList()
    expected = 1

    # act
    sut.add_first(1)
    received = sut.first()

    # assert
    assert expected == received

def test_LinkedList_lastSouldReturNoneIfEmpty():
    # arrange
    sut = LinkedList()
    expected = None

    # act
    received = sut.last()

    # assert
    assert expected == received

def test_LinkedList_lastShouldReturnCorrectValue():
    # arrange
    sut = LinkedList()
    expected = 3

    # act
    sut.add_first(1)
    sut.add_first(2)
    sut.add_last(3)
    received = sut.last()

    # assert
    assert expected == received

def test_delete_first_ShouldDeleteFirstItem():
    # arrange
    sut = LinkedList()
    sut.add_last(1)
    sut.add_last(2)
    sut.add_last(3)

    # act
    deleted_element = sut.delete_first()

    # assert
    assert sut.head.value == 2
    assert deleted_element == 1
    assert sut._length == 2

def test_delete_first_ShouldDeleteOnlyItem():
    # arrange
    sut = LinkedList()
    sut.add_last(1)

    # act
    deleted_element = sut.delete_first()

    # assert
    assert sut.head == None
    assert sut.tail == None
    assert deleted_element == 1
    assert sut._length == 0

def test_delete_first_ShouldReturnNoneForEmptyList():
    # arrange
    sut = LinkedList()

    # act
    deleted_element = sut.delete_first()

    # assert
    assert sut.head == None
    assert sut.tail == None
    assert deleted_element == None
    assert sut._length == 0

def test_delete_last_ShouldRemoveLastItem():
    # arrange
    sut = LinkedList()
    sut.add_last(1)
    sut.add_last(2)
    sut.add_last(3)

    # act
    deleted_element = sut.delete_last()

    # assert
    assert sut.tail.value == 2
    assert deleted_element == 3
    assert sut._length == 2

def test_delete_last_ShouldRemoveOnlyItem():
    # arrange
    sut = LinkedList()
    sut.add_last(1)

    # act
    deleted_element = sut.delete_last()

    # assert
    assert sut.tail == None
    assert sut.head == None
    assert deleted_element == 1
    assert sut._length == 0

def test_delete_last_ShouldReturnNoneForEmptyList():
    # arrange
    sut = LinkedList()

    # act
    deleted_element = sut.delete_last()

    # assert
    assert sut.tail == None
    assert sut.head == None
    assert deleted_element == None
    assert sut._length == 0

def test_delete_at_ShouldRiseIndexErrorWhenInvalidPostion():
    # arrange
    sut = LinkedList()

    # act, assert
    with pytest.raises(IndexError):
        sut.delete_at(0)

def test_delete_at_ShouldRemoveFirstItem():
    # arrange
    sut = LinkedList()
    sut.add_last(1)
    sut.add_last(2)
    sut.add_last(3)

    # act
    sut.delete_at(0)

    # assert
    assert sut.head.value == 2
    assert sut.head.next.value == 3
    assert sut.tail.value == 3
    assert sut._length == 2

def test_delete_at_ShouldRemoveLastItem():
    # arrange
    sut = LinkedList()
    sut.add_last(1)
    sut.add_last(2)
    sut.add_last(3)

    # act
    sut.delete_at(2)

    # assert
    assert sut.head.value == 1
    assert sut.head.next.value == 2
    assert sut.tail.value == 2
    assert sut._length == 2

def test_delete_at_ShouldRemoveMiddleItem():
    # arrange
    sut = LinkedList()
    sut.add_last(1)
    sut.add_last(2)
    sut.add_last(3)
    sut.add_last(4)

    # act
    sut.delete_at(2)
    print(sut)

    # assert
    assert sut.head.value == 1
    assert sut.head.next.value == 2
    assert sut.head.next.next.value == 4
    assert sut.tail.value == 4
    assert sut._length == 3

def test_str_ShouldPrintTheList():
    # arrage
    sut = LinkedList()
    sut.add_last(1)
    sut.add_last(2)
    sut.add_last(3)

    # act
    sut_str = format(sut)

    assert sut_str == "1 -> 2 -> 3"

