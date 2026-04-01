class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, -num)

        if self.minHeap and self.maxHeap and -self.minHeap[0] > self.maxHeap[0]:
            val = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        return (-self.minHeap[0] + self.maxHeap[0]) / 2
        