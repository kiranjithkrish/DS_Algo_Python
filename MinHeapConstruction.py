class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        lastParentIdx = (len(array)-2)//2
        print(range(lastParentIdx))
        if lastParentIdx>0:
            for idx in reversed(range(lastParentIdx+1)):
                self.siftDown(idx, len(array)-1, array) 
        else: 
            self.siftDown(0, len(array)-1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        leftChildIdx = 2*currentIdx+1
        while leftChildIdx<=endIdx:
            rightChildIdx = 2*currentIdx+2 if 2*currentIdx+2<=endIdx else -1
            if rightChildIdx != -1 and heap[leftChildIdx]<heap[rightChildIdx]:
                idxToSwap = leftChildIdx
            else:
                idxToSwap = rightChildIdx
            if heap[idxToSwap]<heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                leftChildIdx = 2*currentIdx+1 
            else:
                break


    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1)//2
        while currentIdx>0 and  self.heap[parentIdx]>self.heap[currentIdx]:
            self.swap(currentIdx,parentIdx, self.heap)
            currentIdx = parentIdx 
            parentIdx = (currentIdx-1)//2
            
    def peek(self):
        return self.heap[0]

    def remove(self):
        #To remove the root value, we swap the root with the last value. Pop the last value now and sift down
        self.swap(0, len(self.heap)-1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
    
    def swap(self, i, j, heap):
        heap[i],heap[j] = heap[j], heap[i]


minHeap = MinHeap( [544, -578, 556, 713, -655, -359, -810, -731, 194, -531, -685, 689, -279, -738, 886, -54, 
            -320, -500, 738, 445, -401, 993, -753, 329, -396, -924, -975, 376, 748, -356, 972, 459, 399, 
            669, -488, 568, -702, 551, 763, -90, -249, -45, 452, -917, 394, 195, -877, 153, 153, 788, 844, 867, 
            266, -739, 904, -154, -947, 464, 343, -312, 150, -656, 528, 
            61, 94, -581])
minHeap.insert(2)

print(minHeap.heap)


