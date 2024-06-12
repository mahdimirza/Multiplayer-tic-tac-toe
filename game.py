from tic_tac_toe_game import ttt_game

class Game:

    def __init__(self, grid_size):
        self.players = 0
        self.gamePlay = ttt_game(grid_size)
        self.grid_size = grid_size
    
    def set_player_1(self, conn, addr):
        self.player1_connection = conn
        self.player1_address = addr
        self.players += 1

    def set_player_2(self, conn, addr): 
        self.player2_connection = conn
        self.player2_address = addr
        self.players += 1

    def get_opponent(self, num):
        if num == 1:
            return(self.player2_address[1])
        else:
            return(self.player1_address[1])
        
    def get_num_players(self):
        return(self.players)
    

    def set_tttGame(self):
        pass