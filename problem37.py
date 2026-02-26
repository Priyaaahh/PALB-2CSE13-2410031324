def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    def dfs(r, c, index):
        if index == len(word):
            return True

        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            board[r][c] != word[index]):
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))

        board[r][c] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


#Example1
board1 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word1 = "ABCCED"
print("Example 1:", exist(board1, word1))  


#Example2
board2 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word2 = "SEE"
print("Example 2:", exist(board2, word2))  


# Example3
board3 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word3 = "ABCB"
print("Example 3:", exist(board3, word3))  
