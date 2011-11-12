from rackoGame import rackoGame
#from pdb import set_trace
import time

gameTime = 0

def start_racko_game(game_id,player_id,initial_discard,other_player_id):
    currentGame = rackoGame(game_id,player_id,initial_discard,other_player_id)
    print "created new racko game with player ID " + str(currentGame.player_id)
    return ''

def get_racko_move(game_id,rack,discard,remaining_microseconds,other_player_moves):
    #if other_player_moves[0][1]['move']=='illegal'
    return discard_algorithm(rack,discard)

def discard_algorithm(rack,discard):
    newLocation = pick_card_location(discard,rack)
    response = {'move':'request_discard','idx':newLocation}
    return response # this is a super dummy move to make, remove when we have brains
    
def get_racko_deck_exchange(game_id,remaining_microseconds,rack,card):
    pick_card_location(card,rack)
    
def pick_card_location(card,rack):
    rackLocation = card/4
    rackLocation = validate_card_location(rackLocation)
    if rackLocation>=0 and rackLocation<=19:
        return rackLocation
    else:
        print "big fucking error: " + str(rackLocation)
        return 7


    
def validate_card_location(rackLocation):
    if rackLocation>=20:
        rackLocation=19
    elif rackLocation<=-1:
        rackLocation = 0
    return rackLocation
    
def get_card_location_by_greater(rack,initLocation,card):
    rackLocation=initLocation
    if rack[initLocation+1]>card:
        rackLocation=initLocation+1
    return rackLocation

def move_racko_result(game_id,move,xmlStruct):
    return ''

def racko_game_result(game_id,your_score,other_score,reason):
    print "Game ended with reason: " + str(reason)
    print "and us scoring: " + str(your_score)
    print "and they scored: " + str(other_score)
    return ''
