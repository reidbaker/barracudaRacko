from rackoGame import rackoGame
import xmlrpclib
from pdb import set_trace

def start_racko_game(game_id,player_id,initial_discard,other_player_id):
    currentGame = rackoGame(game_id,player_id,initial_discard,other_player_id)
    print "created new racko game with player ID " + currentGame.player_id
    return ''

def get_racko_move(game_id,rack,discard,remaining_microseconds,other_player_moves):
    #if other_player_moves[0][1]['move']=='illegal'
    response = {'move':'request_deck'}
    #set_trace()
    return response # this is a super dummy move to make, remove when we have brains
    
def get_racko_deck_exchange(game_id,remaining_microseconds,rack,card):
    return card/4 # again, super dummy

def move_racko_result(game_id,move):
    return ''

def racko_game_result(game_id,your_score,other_score,reason):
    print "Game ended with reason: " + reason + " and us scoring: " + your_score + " and they scored: " + other_score
    return ''
