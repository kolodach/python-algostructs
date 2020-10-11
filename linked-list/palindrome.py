'''Palindrome

Implement a function to check if a linked list is a palindrome.
'''
from linkedlist import LinkedList

def is_palindrome(linkedlist: LinkedList) -> bool:
    '''Determines whether list is a palindrome.

    Args:
      linkedlist: List to check

    Returns:
      True if the list is a palindrome and False otherwise.
    '''
    if len(linkedlist) == 0 or len(linkedlist) == 1:
        return False
    median = int(len(linkedlist) / 2)
    node = linkedlist.head
    half_node = linkedlist.head
    for i in range(len(linkedlist)):
        if i > len(linkedlist) - median and half_node.value != node.value:
            return False
        node = node.next
    return True
