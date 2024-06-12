


class ttt_game:
    def __init__(self, size):
        self.grid_size = size
        self.board = [[' ' for i in range(size)] for j in range(size)]
        self.moved = 0
        self.endgame = False
        self.winner = None
        self.turn = 'O'
    # ////////////////////////////////////////////////////////////////////////////////////////////// 
    def print_board(self):
        response = ''
        for i in range(self.grid_size):
            response += f'{i + 1}|'
            for j in range(self.grid_size):
                response += self.board[i][j]
                response += '|'
            response += '\n'

        return response
    # /////////////////////////////////////////////////////////////////////////////////////////////
    def Update_board(self, action, row, column):
        self.board[row][column] = action
        self.moved += 1

    # /////////////////////////////////////////////////////////////////////////////////////////////

    def Row_win_3(self, action):
        for i in range(self.grid_size):
            flag = True
            for j in range(self.grid_size):
                if(self.board[i][j] != action):
                    flag = False
                    break
            if(flag):
                return(True)
            
        return(flag)
    # /////////////////////////////////////////////////////////////////////////////////////////////

    def Column_win_3(self, action):
        for i in range(self.grid_size):
            flag = True
            for j in range(self.grid_size):
                if(self.board[j][i] != action):
                    flag = False
                    break
            if(flag):
                return(True)
            
        return(flag)
    # //////////////////////////////////////////////////////////////////////////////////////////////

    def Diagonal_win_3(self, action):
        flag = True
        for i in range(self.grid_size):
            if(self.board[i][i] != action):
                flag = False
                break

        if(flag):
            return(flag)

        flag = True
        for i in range(self.grid_size):
            x = self.grid_size - 1 - i
            if(self.board[i][x] != action):
                flag = False
                break
        
        return(flag)
    # //////////////////////////////////////////////////////////////////////////////////////////////
    def Row_win_4(self, action):
        flag = 0
        for i in range(len(self.board)):
            if(self.board[i][0] == self.board[i][1] == self.board[i][2] == action):
                flag = 1
                return(True)

            elif(self.board[i][1] == self.board[i][2] == self.board[i][3] == action):
                flag = 1
                return True
            
        if(flag == 0):
            return(False)
    # //////////////////////////////////////////////////////////////////////////////////////////////
        
    def Column_win_4(self, action):
        flag = 0
        for i in range(len(self.board)):
            if(self.board[0][i] == self.board[1][i] == self.board[2][i] == action):
                flag = 1
                return(True)

            elif(self.board[1][i] == self.board[2][i] == self.board[3][i] == action):
                flag = 1
                return True
            
        if(flag == 0):
            return(False)
        
    #///////////////////////////////////////////////////////////////////////////////////////////////
        
    def Diagonal_win_4(self, action):

        flag = 0
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] == action):
            flag = 1
            return(True)
        elif(self.board[1][1] == self.board[2][2] == self.board[3][3] == action):
            flag = 1
            return(True)
        elif(self.board[0][3] == self.board[1][2] == self.board[2][1] == action):
            flag = 1
            return(True)
        elif(self.board[1][2] == self.board[2][1] == self.board[3][0] == action):
            flag = 1
            return(True)

        if(flag == 0):
            return(False)
        

    # ////////////////////////////////////////////////////////////////////////////////////////////////
        
    def Row_win_5(self, action):
        flag = 0
        
        for i in range(len(self.board)):
            if(self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] == action):
                flag = 1
                return(True)

            elif(self.board[i][1] == self.board[i][2] == self.board[i][3] == self.board[i][4] == action):
                flag = 1
                return True
            
        if(flag == 0):
            return(False)
    # /////////////////////////////////////////////////////////////////////////////////////////////////
        
    def Column_win_5(self, action):
        flag = 0
        for i in range(len(self.board)):
            if(self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] ==action):
                flag = 1
                return(True)

            elif(self.board[1][i] == self.board[2][i] == self.board[3][i] == self.board[4][i] ==action):
                flag = 1
                return True
            
        if(flag == 0):
            return(False)
        
    # /////////////////////////////////////////////////////////////////////////////////////////////////
        
    def Diagonal_win_5(self, action):

        flag = 0
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == action):
            flag = 1
            return(True)
        elif(self.board[1][1] == self.board[2][2] == self.board[3][3] == self.board[4][4] == action):
            flag = 1
            return(True)
        elif(self.board[0][4] == self.board[1][3] == self.board[2][2] == self.board[3][1] == action):
            flag = 1
            return(True)
        elif(self.board[1][3] == self.board[2][2] == self.board[3][1] == self.board[4][0] == action):
            flag = 1
            return(True)

        if(flag == 0):
            return(False)
        

        
