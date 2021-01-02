# Link: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next
