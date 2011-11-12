from rackoGame import rackoGame
import xmlrpclib
from pdb import set_trace
from naiveAgent import naiveAgent

currentAgent = None

def start_racko_game(game_id,player_id,initial_discard,other_player_id):
    currentGame = rackoGame(game_id,player_id,initial_discard,other_player_id)
    print "created new racko game with player ID " + str(currentGame.player_id)
    global currentAgent
    currentAgent = naiveAgent(currentGame)
    return ''

def get_racko_move(game_id,rack,discard,remaining_microseconds,other_player_moves):
    #if other_player_moves[0][1]['move']=='illegal'
    global currentAgent
    action = currentAgent.getAction(other_player_moves)
    return action # this is a super dummy move to make, remove when we have brains
    
def get_racko_deck_exchange(game_id,remaining_microseconds,rack,card):
    global currentAgent
    response = currentAgent.drawCard(card)
    return response

def move_racko_result(game_id,move,xmlStruct):
    return ''

def racko_game_result(game_id,your_score,other_score,reason):
    print "Game ended with reason: " + str(reason)
    print "and us scoring: " + str(your_score)
    print "and they scored: " + str(other_score)
    return ''
