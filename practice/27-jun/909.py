class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Get length of the board
        length = len(board)
        # reverse the board to acces the last row at first
        board.reverse()
        
        # integer to position on the board
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        # BFS for the moves to explore all possible outcomes    
        q = deque()
        q.append([1, 0]) # [square, moves]
        visit = set()
        while q:
            # Pop from the q
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                # if value at [r,c] is not -1 then take value of [r, c]
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                # If we reach the last square then inc moves by 1
                if nextSquare == length * length:
                    return moves + 1
                # If nextSquare not in visit then add it to the set
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    # append nextSquare and inc move count 
                    q.append([nextSquare, moves + 1])
        return -1