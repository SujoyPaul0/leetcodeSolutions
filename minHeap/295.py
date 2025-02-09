'''
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
'''

class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        #heaps should be equal size
        # small is maxheap and large is minheap(python default)
        self.small, self.large = [], [] 

    def addNum(self, num: int) -> None:
        # if num is > than min of large(0th index of min heap) push it to large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        # else push it to small but multiply num with -1 as it is maxheap
        else:
            heapq.heappush(self.small, -1*num)

        # check if length of one heap is more than 2 of other
        if len(self.small) > len(self.large) + 1:
            # then pop(which is max of maxheap) from small and push it to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # if length of large > small
        if len(self.large) > len(self.small):
        # pop from large and push it to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        

    def findMedian(self) -> float:
        # if length of small is > length of large then the max of small is median
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # else if the opposite
        elif len(self.large) > len(self.small):
            return self.large[0]
        # else both length is equal
        return (-1 * self.small[0] + self.large[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()