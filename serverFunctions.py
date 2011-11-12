from rackoGame import rackoGame
import xmlrpclib
from pdb import set_trace

def start_racko_game(game_id,player_id,initial_discard,other_player_id):
    currentGame = rackoGame(game_id,player_id,initial_discard,other_player_id)
    print "created new racko game with player ID " + str(currentGame.player_id)
    return ''

def get_racko_move(game_id,rack,discard,remaining_microseconds,other_player_moves):
    #if other_player_moves[0][1]['move']=='illegal'
    response = {'move':'request_deck'}
    return response # this is a super dummy move to make, remove when we have brains
    
def get_racko_deck_exchange(game_id,remaining_microseconds,rack,card):
    response = card/4
#    if rack[response]<card:
#        for i in range(0,len(range))
    if response>=20:
        response=19
    elif response<=-1:
        response = 0
    
    if response>=0 and response<=19:
        return response
    else:
        print "big fucking error: " + str(response)
        return 7

def move_racko_result(game_id,move,xmlStruct):
    return ''

def racko_game_result(game_id,your_score,other_score,reason):
    print "Game ended with reason: " + str(reason)
    print "and us scoring: " + str(your_score)
    print "and they scored: " + str(other_score)
    return ''
