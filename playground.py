from rackoGame import rackoGame
from pdb import set_trace
import time

gameTime = 0
turn = 0
turnLimit = 20
#isSorted = lambda l : all(a <= b for a,b in __import__("itertools").izip(l[:-1],l[1:]))

def isSorted(list):
    copy = list[:]
    copy.sort()
    for i in range(0,len(list)):
        if list[i] is not copy[i]:
            return False
    return True

def start_racko_game(game_id,player_id,initial_discard,other_player_id):
    currentGame = rackoGame(game_id,player_id,initial_discard,other_player_id)
    global turn
    turn = 0
    print "created new racko game with player ID " + str(currentGame.player_id)
    return ''

def get_racko_move(game_id,rack,discard,remaining_microseconds,other_player_moves):
    global turn
    global turnLimit
    turn += 1
    if turn>turnLimit:
        middleIndex = find_middles(rack,discard)
        addConsecutive = find_good_streak(rack,discard)
        if addConsecutive:
            return {'move':'request_discard','idx':addConsecutive}
        elif middleIndex:
            return {'move':'request_discard','idx':middleIndex}
        else:
            return from_deck_algorithm()
    else:
        middleIndex = find_middles(rack,discard)
        if middleIndex:
            return {'move':'request_discard','idx':middleIndex}
        else:
            return from_deck_algorithm()
        
    
def find_good_streak(rack,card):
    for i in range(0,len(rack)):
        streak = is_in_streak(rack, i)
        if streak[0]:
            if rack[streak[0]]==card+1:
                out = streak[0]-1
                if out<0:
                    out = 0
                return out
        if streak[1]:
            if rack[streak[1]]==card-1:
                out = streak[1]+1
                if out>19:
                    out = 19
                return out
    return None

def discard_algorithm(rack,discard):
    newLocation = pick_card_location(discard,rack)
    response = {'move':'request_discard','idx':newLocation}
    return response # this is a super dummy move to make, remove when we have brains

def find_middles(rack,discard):
    for i in range(1,len(rack)-1):
        if discard>rack[i-1] and discard<rack[i+1]: # check to see if discard card fits between window
            if rack[i]<rack[i-1] or rack[i]>rack[i+1]: # check to see if middle of window is out of place
                return i
    return None

def from_deck_algorithm():
    return {'move':'request_deck'}
    
def get_racko_deck_exchange(game_id,remaining_microseconds,rack,card):
    global turn
    global turnLimit
    if turn>turnLimit:
        middleIndex = find_middles(rack,card)
        streak = find_good_streak(rack,card)
        if streak:
            return streak
        elif middleIndex:
            return middleIndex
        else:
            return buncher_algorithm(card,rack)
    else:
        middleIndex = find_middles(rack,card)
        if middleIndex:
            return middleIndex
        else:
            return buncher_algorithm(card,rack)
        

    
def pick_card_location(card,rack):
    rackLocation = (card)/4
    rackLocation = validate_card_location(rackLocation)
    if rackLocation>=0 and rackLocation<=19:
        streak = is_in_streak(rack,rackLocation)
        if streak[0]:
            return streak[0]-1
        return rackLocation
    else:
        print "big fucking error: " + str(rackLocation)
        return 7

def buncher_algorithm(card,rack):
    initLocation = pick_card_location(card,rack)
    if isSorted(rack):
        greaterLocation =  get_card_location_by_greater(rack,initLocation,card)
        streakRange = is_in_streak(rack,greaterLocation)
        if streakRange[0]:
            if (streakRange[0]==greaterLocation) and not (streakRange[1]==greaterLocation):
                return streakRange[0]-1
        else:
            return greaterLocation
    else:
        return initLocation
    
def validate_card_location(rackLocation):
    if rackLocation>=20:
        rackLocation=19
    elif rackLocation<=-1:
        rackLocation = 0
    return rackLocation

def position_in_streak(rack,location):
    startingPoint = location
    lowestLocation = location - 4
    if lowestLocation < 0:
        lowestLocation=0
    for i in range(lowestLocation,location+1).reverse():
        if rack[i]==rack[i+1]+1:
            startingPoint = i
        else:
            break
    return location-startingPoint

def is_in_streak(rack,location):
    return (find_start_of_streak(rack,location),find_end_of_streak(rack,location))

def find_start_of_streak(rack,location):
    startingPoint = None
    checkRange = range(0,location)
    checkRange.reverse()
    for i in checkRange:
        if rack[i]==rack[i+1]-1:
            startingPoint = i
        else:
            break
    return startingPoint

def find_end_of_streak(rack,location):
    endingPoint = None
    if location==len(rack)-1:
        location = len(rack)-2
    for i in range(location+1,len(rack)):
        if rack[i]==rack[i-1]+1:
            endingPoint = i
        else:
            break
    return endingPoint

def get_card_location_by_greater(rack,initLocation,card):
    rackLocation=len(rack)-1
    for i in range(initLocation,len(rack)):
        if rack[i]>card:
            rackLocation=i
            break
    return rackLocation

def move_racko_result(game_id,move,xmlStruct):
    print xmlStruct
    return ''

def racko_game_result(game_id,your_score,other_score,reason):
    print "Game ended with reason: " + str(reason)
    print "and us scoring: " + str(your_score)
    print "and they scored: " + str(other_score)
    return ''
