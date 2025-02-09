'''
Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        # count no of chr in task and add it to hashmap
        count = Counter(tasks)
        # create a maxheap with -ve values in count as py supports only minheap
        maxHeap = [-cnt for cnt in count.values()]
        # create heap
        heapq.heapify(maxHeap)

        time = 0
        # a queue with -cnt and the time when cnt can be processed
        q = deque() # pairs of [-cnt, idleTime]

        # while maxHeap or q not empty
        while maxHeap or q:
            # 
            time += 1

            # if maxHeap is not empty
            if maxHeap:
                # as we took -ve values of cnt so we have to add 1 to decrement it
                cnt = 1 + heapq.heappop(maxHeap)
                # if cnt is not 0 add it to queue
                if cnt:
                    q.append([cnt, time + n])
            # if idle time of first element in q is met
            if q and q[0][1] == time:
                # add it to maxhaep
                heapq.heappush(maxHeap, q.popleft()[0])
        return time