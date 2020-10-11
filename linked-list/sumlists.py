'''Sum Lists Problem

You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit is
at the head of the list. Write a function that adds the two numbers and returns
the sum as a linked list.

Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295. Output:
2 -> 1 -> 9.That is, 912.

Suppose the digits are stored in forward order. Repeat the above problem.
'''
from linkedlist import LinkedList

def sum_lists(first: LinkedList, second: LinkedList):
    result = LinkedList()
    first_node = first.head
    second_node = second.head
    next_column = 0
    while first_node != None or second_node != None or next_column != 0:
        first_node_value = first_node.value if first_node else 0
        second_node_value = second_node.value if second_node else 0
        node_sum = first_node_value + second_node_value + next_column
        next_column = 0
        if node_sum >= 10:
            next_column = 1
            node_sum = node_sum - 10
        result.add_last(node_sum)
        first_node = first_node.next if first_node else None
        second_node = second_node.next if second_node else None
    return result
