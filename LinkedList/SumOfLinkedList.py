# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    factor = 1
    sumOne = 0
    sumTwo = 0

    while linkedListOne is not None:
        sumOne += linkedListOne.value * factor
        factor *= 10
        linkedListOne = linkedListOne.next
    factor = 1
    while linkedListTwo is not None:
        sumTwo += linkedListTwo.value * factor
        factor *= 10
        linkedListTwo = linkedListTwo.next
    totalSum = sumOne + sumTwo
    prev = None
    head = None
    current = None
    if totalSum == 0:
        head = LinkedList(0)
        head.next = None
        return head
    while totalSum > 0:
        remainder = totalSum % 10
        totalSum = totalSum // 10
        if head is None:
            head = LinkedList(remainder)
            current = head
        else:
            current.next = LinkedList(remainder)
            current = current.next
    return head


listOne = LinkedList(0)
# listOne.next = LinkedList(4)
# listOne.next.next = LinkedList(7)
# listOne.next.next.next = LinkedList(1)

listTwo = LinkedList(0)
# listTwo.next = LinkedList(4)
# listTwo.next.next = LinkedList(5)

sum = sumOfLinkedLists(listOne, listTwo)
