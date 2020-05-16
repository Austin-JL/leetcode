class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not word :
            return False
        
        # i row number and j col number 
        
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if self.dfs(board,word,i,j):
                    return True
        return False
    
    def dfs(self, board, word,i,j):
        # check first letter of word 
        if board[i][j] == word[0] :
            res = word[1:]
            if not res :
                return True
            # mark visited 
            board[i][j] = " "
            # dfs the board
            if i > 0 and self.dfs(board,res,i-1,j):
                return True
            if i < len(board)-1 and self.dfs(board,res,i+1,j):
                return True
            if j > 0 and self.dfs(board,res,i,j-1):
                return True
            if j < len(board[0])-1 and self.dfs(board,res,i,j+1):
                return True
            
            # restore board
            board[i][j] = word[0]
            return False
        else:
            return False
        
        