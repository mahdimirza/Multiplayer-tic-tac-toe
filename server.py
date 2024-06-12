# echo-server.py

import socket
import threading
from game import Game
from tic_tac_toe_game import ttt_game


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 34134  # Port to listen on (non-privileged ports are > 1023)


games_3 = list()
games_4 = list()
games_5 = list()
games = list()
games.append(games_3)
games.append(games_4)
games.append(games_5)





def end_match(gameplay):

    if(gameplay.grid_size == 3):

        if(gameplay.Row_win_3('X') or gameplay.Column_win_3('X') or gameplay.Diagonal_win_3('X')):
            gameplay.winner = 'X'
            return(True)
        elif(gameplay.Row_win_3('O') or gameplay.Column_win_3('O') or gameplay.Diagonal_win_3('O')):
            gameplay.winner = 'O'
            return(True)
        elif(gameplay.moved == gameplay.grid_size ** 2) :
            gameplay.winner = 'Draw'
            return(True)
        else:
            return(False)
        
    elif(gameplay.grid_size == 4):

        if(gameplay.Row_win_4('X') or gameplay.Column_win_4('X') or gameplay.Diagonal_win_4('X')):
            gameplay.winner = 'X'
            return(True)
        elif(gameplay.Row_win_4('O') or gameplay.Column_win_4('O') or gameplay.Diagonal_win_4('O')):
            gameplay.winner = 'O'
            return(True)
        elif(gameplay.moved == gameplay.grid_size ** 2) :
            gameplay.winner = 'Draw'
            return(True)
        else:
            return(False)
        
    elif(gameplay.grid_size == 5):

        if(gameplay.Row_win_5('X') or gameplay.Column_win_5('X') or gameplay.Diagonal_win_5('X')):
            gameplay.winner = 'X'
            return(True)
        elif(gameplay.Row_win_5('O') or gameplay.Column_win_5('O') or gameplay.Diagonal_win_5('O')):
            gameplay.winner = 'O'
            return(True)
        elif(gameplay.moved == gameplay.grid_size ** 2) :
            gameplay.winner = 'Draw'
            return(True)
        else:
            return(False)


def play_game(gamePlay,  playernumber, conn):
    player = None
    if(playernumber == 1):
        player = 'X'
    else:
        player = 'O'

    while(gamePlay.moved != gamePlay.grid_size ** 2) :
        while(gamePlay.turn == player):
            continue

        
        if(end_match(gamePlay) == False):
            

            msg = gamePlay.print_board()
            msg += '\nit is your turn\n'
            conn.send(msg.encode())

            msg = conn.recv(1024)
            msg = msg.split()
            msg[0] = int(msg[0]) - 1
            msg[1] = int(msg[1]) - 1

            gamePlay.Update_board(player, msg[0], msg[1])

            gamePlay.turn = player

        else:
            msg = '\nend Match\n'
            if(gamePlay.winner == 'Draw'):
                msg += '\n' + gamePlay.winner + '\n'
                conn.send(msg.encode())

            else:
                msg += '\nplayer ' + gamePlay.winner + ' wins\n'
                conn.send(msg.encode())
            gamePlay.turn = player
            return()
        
    msg = '\nend Match\n'
    msg += '\n' + gamePlay.winner + '\n'
    conn.send(msg.encode())
    return()
    






def find_opponent(grid_size):
    if(len(games[grid_size - 3]) == 0 or games[grid_size - 3][-1].get_num_players() == 2):
        g = Game(grid_size)
        games[grid_size - 3].append(g)
        return(g)
    elif(games[grid_size - 3][-1].get_num_players() == 1):
        return(games[grid_size - 3][-1])
    



def handle_connection(conn, addr): 
    with conn:

        msg = 'which size you want to play? (3, 4 or 5)'
        conn.send(msg.encode())
        msg = conn.recv(1024)

        grid_size = int(msg)


        print(f"Connected by {addr[1]}")
        NewGame = find_opponent(grid_size)


        playernumber = 0
        if(NewGame.get_num_players() == 0):
            playernumber = 1
            NewGame.set_player_1(conn, addr)
            msg = 'wait'.encode()
            conn.send(msg)
            while(NewGame.get_num_players() == 1):
                continue


            msg = f'your opponent is{NewGame.get_opponent(1)}\n'
            msg += 'you are (X)\n'
            conn.send(msg.encode())

            play_game(NewGame.gamePlay, 1, conn)

        else:
            playernumber = 2
            NewGame.set_player_2(conn,addr)
            msg = f'your opponent is{NewGame.get_opponent(2)}\n'
            msg += 'you are (O)\n'
            conn.send(msg.encode())

            play_game(NewGame.gamePlay, 2, conn)
 



        





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    print("Waiting for clients...")
    while(1):
        conn, addr = s.accept()
        print(f'client connected with ip -> {addr[1]}')
        thread = threading.Thread(target=handle_connection, args=(conn,addr))
        thread.start()

    s.close()