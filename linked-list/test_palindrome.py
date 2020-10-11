from linkedlist import LinkedList
from palindrome import is_palindrome

def test_is_palindrome_ShouldRetrunTrueIfPalindromeEvenLength():
    # arrange
    sut = LinkedList()
    sut.add_first("a")
    sut.add_first("b")
    sut.add_first("b")
    sut.add_first("a")

    # act
    result = is_palindrome(sut)

    # assert
    assert result == True

def test_is_palindrome_ShouldRetrunTrueIfPalindromeOddLength():
    # arrange
    sut = LinkedList()
    sut.add_first("a")
    sut.add_first("b")
    sut.add_first("c")
    sut.add_first("b")
    sut.add_first("a")

    # act
    result = is_palindrome(sut)

    # assert
    assert result == True

def test_is_palindrome_ShoulRetrunFalseIfNotPalindrome():
    # arrange
    sut = LinkedList()
    sut.add_first("a")
    sut.add_first("b")
    sut.add_first("b")
    sut.add_first("d")

    # act
    result = is_palindrome(sut)

    # assert
    assert result == False

def test_is_palindrome_ShouldRetrunFalseIfEmpty():
    # arrange
    sut = LinkedList()

    # act
    result = is_palindrome(sut)

    # assert
    assert result == False
