from SimpleXMLRPCServer import SimpleXMLRPCServer
from serverFunctions import *
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
server = SimpleXMLRPCServer(('172.16.89.213', 80), logRequests=True)

# Expose a function
def ping(message):
    """
    """
    if message=='ping':
        return 'pong'
    else:
        return ''
    
server.register_function(ping)

def start_game(game_id,player_id,initial_discard,other_player_id):
    return start_racko_game(game_id,player_id,initial_discard,other_player_id)

def get_move(game_id,rack,discard,remaining_microseconds,other_player_moves):
    return get_racko_move(game_id,rack,discard,remaining_microseconds,other_player_moves)

def get_deck_exchange(game_id,remaining_microseconds,rack,card):
    return get_racko_deck_exchange(game_id,remaining_microseconds,rack,card)

def move_result(game_id,move):
    return move_racko_result(game_id,move)

def game_result(game_id,your_score,other_score,reason):
    return racko_game_result(game_id,your_score,other_score,reason)


try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'