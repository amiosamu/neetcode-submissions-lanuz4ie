class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        minHeap = []
        currPassengers = 0
        for numPassengers, pickup, drop in trips:
            while minHeap and minHeap[0][0] <= pickup:
                dropLoc, passengers = heapq.heappop(minHeap)
                currPassengers -= passengers
            currPassengers += numPassengers
            if currPassengers > capacity:
                return False
            heapq.heappush(minHeap, (drop, numPassengers))
        return True
