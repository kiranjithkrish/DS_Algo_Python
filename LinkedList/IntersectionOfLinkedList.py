class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def lenght_of_list(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length


def mergingLinkedListsOne(linkedListOne, linkedListTwo):
    nodeSet = set()
    while linkedListOne is not None:
        nodeSet.add(linkedListOne)
        linkedListOne = linkedListOne.next

    while linkedListTwo is not None:
        if linkedListTwo in nodeSet:
            return linkedListTwo
        linkedListTwo = linkedListTwo.next
    return None


def mergingLinkedListsTwo(linkedListOne, linkedListTwo):
    listOneLength = lenght_of_list(linkedListOne)
    listTwoLength = lenght_of_list(linkedListTwo)
    difference = abs(listOneLength - listTwoLength)
    longerList = linkedListOne if listOneLength > listTwoLength else linkedListTwo
    shorterList = linkedListTwo if listOneLength > listTwoLength else linkedListOne
    while difference > 0:
        difference -= 1
        longerList = longerList.next
    while longerList is not None and longerList.value != shorterList.value:
        longerList = longerList.next
        shorterList = shorterList.next
    return longerList


def mergingLinkedListsThree(linkedListOne, linkedListTwo):
    currentOne = linkedListOne
    currentTwo = linkedListTwo
    while currentOne is not currentTwo:
        if currentOne is None:
            currentOne = linkedListTwo
        else:
            currentOne = currentOne.next
        if currentTwo is None:
            currentTwo = linkedListOne
        else:
            currentTwo = currentTwo.next
    return currentOne


listOne = LinkedList(1)
listOne.next = LinkedList(2)
# listOne.next.next = LinkedList(7)
# listOne.next.next.next = LinkedList(1)

listTwo = LinkedList(4)
listTwo.next = LinkedList(2)
# listTwo.next.next = LinkedList(5)

mergingLinkedListsTwo(listOne, listTwo)
