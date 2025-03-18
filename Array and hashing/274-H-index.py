'''
Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h_index = 0
        for i, citation in enumerate(citations):
            #check if at least (i+1) papers have(i+1) or more citations
            if citation >= i + 1:
                h_index = i + 1
            else: 
                break
        return h_index
        