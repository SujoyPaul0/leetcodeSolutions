'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals based on the start time
        # Sorting ensures that overlapping intervals are next to each other.
        intervals.sort(key = lambda pair: pair[0])

        # Step 2: Initialize the output list with the first interval
        output = [intervals[0]]

        # step 3: Iterate through the sorted intervals
        for start, end in intervals:
            lastEnd = output[-1][1] # Get the end time of the last interval in output

            if start <= lastEnd:
                # Step 4: If the current interval overlaps with the last interval in output
                # Merge them by updating the end time to the maximum end time
                output[-1][1] = max(lastEnd, end)
            else:
                # step 5: if no overlap, add the new interval as a separate entry
                output.append([start, end])

        # Step 6: Return the merged intervals
        return output