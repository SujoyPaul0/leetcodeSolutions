'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # taking -ve values of every ele of stones
        stones = [-s for s in stones] 
        # to create minheap with -ve value which is maxheap
        heapq.heapify(stones) 

        # iterating by len of stones
        while len(stones) > 1:
            # first is first pop which is min but the max if +
            first = heapq.heappop(stones)
            # second is second smallest in min heap
            second = heapq.heappop(stones)
            # if second > first while values are -ve
            if second > first:
                # push (first - second) in the heap
                heapq.heappush(stones, first - second)

        # in stones we append 0
        stones.append(0)
        # return abs or + value of stones[0]
        return abs(stones[0])
