




def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r,c,index):

        if index == len(word):
            return True
        
        # boundary mismatch

        if (r < 0 or c < 0 or
            r >= rows or c >= cols or
             board[r][c] != word[index] ):
            return False
        
        temp = board[r][c]
        board[r][c] = "#" #mark visited

        found = (
            dfs(r + 1, c , index + 1) or
               (r - 1, c , index + 1) or
               (r, c + 1 , index + 1) or
               (r, c - 1 , index + 1)
        )

        board[r][c] = temp
        return found
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if dfs(r,c,0):
                    return True
    return False
