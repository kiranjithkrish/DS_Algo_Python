class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        lastParentIdx = (len(array) - 2) // 2
        for idx in reversed(range(lastParentIdx + 1)):
            self.siftDown(idx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        leftChildIdx = 2 * currentIdx + 1
        while leftChildIdx <= endIdx:
            rightChildIdx = 2 * currentIdx + 2 if 2 * currentIdx + 2 <= endIdx else -1
            if rightChildIdx != -1 and heap[rightChildIdx] < heap[leftChildIdx]:
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                leftChildIdx = 2 * currentIdx + 1
            else:
                break

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and self.heap[parentIdx] > self.heap[currentIdx]:
            self.swap(currentIdx, parentIdx, self.heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        # To remove the root value, we swap the root with the last value. Pop the last value now and sift down
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


minHeap = MinHeap(
    [
        -823,
        164,
        48,
        -987,
        323,
        399,
        -293,
        183,
        -908,
        -376,
        14,
        980,
        965,
        842,
        422,
        829,
        59,
        724,
        -415,
        -733,
        356,
        -855,
        -155,
        52,
        328,
        -544,
        -371,
        -160,
        -942,
        -51,
        700,
        -363,
        -353,
        -359,
        238,
        892,
        -730,
        -575,
        892,
        490,
        490,
        995,
        572,
        888,
        -935,
        919,
        -191,
        646,
        -120,
        125,
        -817,
        341,
        -575,
        372,
        -874,
        243,
        610,
        -36,
        -685,
        -337,
        -13,
        295,
        800,
        -950,
        -949,
        -257,
        631,
        -542,
        201,
        -796,
        157,
        950,
        540,
        -846,
        -265,
        746,
        355,
        -578,
        -441,
        -254,
        -941,
        -738,
        -469,
        -167,
        -420,
        -126,
        -410,
        59,
    ]
)
# minHeap.insert(2)

print(minHeap.heap)
