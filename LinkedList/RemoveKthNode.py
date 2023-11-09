# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    lengthOfList = lenght_of_list(head)
    removeAt = lengthOfList - k
    if head is not None:
        return removeNodeAt(head, removeAt)


def removeKthNodeFromEndApproachTwo(head, k):
    first = head
    second = head
    count = 1
    while count <= k:
        second = second.next
        count += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return head
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
    return head


def lenght_of_list(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length


def removeNodeAt(head, m):
    prev = None
    current = head
    length = 0
    if m == 0:
        head.value = head.next.value
        head.next = head.next.next
    while current.next is not None:
        length += 1
        prev = current
        current = current.next
        next = current.next
        if length is m:
            prev.next = next


# The better approach is below


head = LinkedList(value=0)
head.next = LinkedList(value=1)
head.next.next = LinkedList(value=2)
head.next.next.next = LinkedList(value=3)
head.next.next.next.next = LinkedList(value=4)
head.next.next.next.next.next = LinkedList(value=5)
head.next.next.next.next.next.next = LinkedList(value=6)
head.next.next.next.next.next.next.next = LinkedList(value=7)
head.next.next.next.next.next.next.next.next = LinkedList(value=8)
head.next.next.next.next.next.next.next.next.next = LinkedList(value=9)
print(lenght_of_list(head))
head = removeKthNodeFromEndApproachTwo(head, 10)
print(lenght_of_list(head))
