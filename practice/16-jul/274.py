class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        count = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                count = i + 1

            else:
                break

        return count