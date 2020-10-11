from linkedlist import LinkedList
from sumlists import sum_lists

def test_sumlists_ShouldReturnCorrectSum():
    # arrange
    first = LinkedList()
    first.add_first(6)
    first.add_first(1)
    first.add_first(7)
    second = LinkedList()
    second.add_first(2)
    second.add_first(9)
    second.add_first(5)

    # act
    result = sum_lists(first, second)

    # assert
    assert len(result) == 3
    assert result.head.value == 2
    assert result.head.next.value == 1
    assert result.head.next.next.value == 9
    assert result.tail.value == 9
    assert result.head.next.next.next == None

def test_sumlists_ShouldReturnSumIfFirstIsGreater():
    # arrange
    first = LinkedList()
    first.add_first(6)
    first.add_first(1)
    first.add_first(7)
    first.add_first(9)
    second = LinkedList()
    second.add_first(2)
    second.add_first(9)

    # act
    result = sum_lists(first, second)

    # assert
    assert len(result) == 4
    assert result.head.value == 8
    assert result.head.next.value == 0
    assert result.head.next.next.value == 2
    assert result.head.next.next.next.value == 6
    assert result.tail.value == 6
    assert result.head.next.next.next.next == None

def test_sumlists_ShouldReturnSumIfSecondGreater():
    # arrange
    first = LinkedList()
    first.add_first(2)
    first.add_first(9)
    second = LinkedList()
    second.add_first(6)
    second.add_first(1)
    second.add_first(7)
    second.add_first(9)

    # act
    result = sum_lists(first, second)

    # assert
    assert len(result) == 4
    assert result.head.value == 8
    assert result.head.next.value == 0
    assert result.head.next.next.value == 2
    assert result.head.next.next.next.value == 6
    assert result.tail.value == 6
    assert result.head.next.next.next.next == None

def test_sumlists_ShouldSumIfFirstEmpty():
    # arrange
    first = LinkedList()
    first.add_first(2)
    first.add_first(9)
    second = LinkedList()

    # act
    result = sum_lists(first, second)

    # assert
    assert len(result) == 2
    assert result.head.value == 9
    assert result.head.next.value == 2
    assert result.tail.value == 2
    assert result.head.next.next == None

def test_sumlists_ShouldSumIfSecondEmpty():
    # arrange
    first = LinkedList()
    second = LinkedList()
    second.add_first(2)
    second.add_first(9)

    # act
    result = sum_lists(first, second)

    # assert
    assert len(result) == 2
    assert result.head.value == 9
    assert result.head.next.value == 2
    assert result.tail.value == 2
    assert result.head.next.next == None
