class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for n in nums:
            heapq.heappush(maxHeap, -n)

        res = 0
        while k > 0:
            res = heapq.heappop(maxHeap)
            k -= 1
            
        return -res