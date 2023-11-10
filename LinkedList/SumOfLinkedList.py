# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedListsOptimisedAgain(linkedListOne, linkedListTwo):
    currentOne = linkedListOne
    currentTwo = linkedListTwo
    head = None
    current = head
    sum = 0
    carry = 0
    while currentOne is not None or currentTwo is not None:
        sumOne = currentOne.value if currentOne is not None else 0
        sumTwo = currentTwo.value if currentTwo is not None else 0
        sum = sumOne + sumTwo + carry
        sumValueForList = sum % 10
        carry = sum // 10 if sum > 9 else 0
        if head is None:
            head = LinkedList(sumValueForList)
            current = head
        else:
            current.next = LinkedList(sumValueForList)
            current = current.next
        if carry > 0:
            lastNode = LinkedList(carry)
            lastNode.next = None
            current.next = lastNode
        currentOne = currentOne.next if currentOne is not None else None
        currentTwo = currentTwo.next if currentTwo is not None else None
    return head


def sumOfLinkedListsOptimised(linkedListOne, linkedListTwo):
    headOne = linkedListOne
    headTwo = linkedListTwo
    currentOne = headOne
    currentTwo = headTwo
    sum = 0
    totalSum = 0
    factor = 1
    carry = 0
    while currentOne is not None or currentTwo is not None:
        sumOne = currentOne.value * factor if currentOne is not None else 0
        sumTwo = currentTwo.value * factor if currentTwo is not None else 0
        sum = sumOne + sumTwo
        totalSum += sum
        factor *= 10
        currentOne = currentOne.next if currentOne is not None else None
        currentTwo = currentTwo.next if currentTwo is not None else None
    return generateLinkedListFromInteger(totalSum)


def lenght_of_list(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length


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
    return generateLinkedListFromInteger(totalSum)


def generateLinkedListFromInteger(n):
    while n > 0:
        remainder = n % 10
        n = n // 10
        if head is None:
            head = LinkedList(remainder)
            current = head
        else:
            current.next = LinkedList(remainder)
            current = current.next
    return head


listOne = LinkedList(2)
listOne.next = LinkedList(4)
listOne.next.next = LinkedList(7)
listOne.next.next.next = LinkedList(1)

listTwo = LinkedList(9)
listTwo.next = LinkedList(4)
listTwo.next.next = LinkedList(5)

sum = sumOfLinkedListsOptimisedAgain(listOne, listTwo)
print(sum)
