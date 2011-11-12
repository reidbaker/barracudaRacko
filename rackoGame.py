class rackoGame(object):
    def __init__(self,game_id,player_id,initial_discard,other_player_id):
        """
        constructor for a rackoGame
        initializes all necessary data
        """
        self.game_id = game_id
        self.player_id = player_id
        self.discard_pile = [initial_discard]
        self.other_player_id = other_player_id
        self.current_rack = []
        self.opponent_rack = []
        self.unknown_cards = [] # should be the 59 cards NOT in the discard_pile + current_rack
    def drawDiscard(self,card):
        """
        draw a card from the pile
        returns the top card of the pile
        """
        return self.discard_pile.pop()
    def switchCard(self,card,newPos):
        """
        switch a card out of my rack
        discards the card switched out and puts the new card in the rack
        at the position specified by 'newPos'
        """
        self.discard_pile.append(self.current_rack[newPos])
        self.current_rack[newPos]=card
    def switchOpponentCard(self,card,newPos):
        """
        switch a card out of an opponent's rack
        same functionality as switchCard def
        """
        self.discard_pile.append(self.opponent_rack[newPos])
        self.opponent_rack[newPos]=card