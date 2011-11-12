import math

def goodness(a,b,c):
    return (1 if math.floor((a.value-.5)/4)==c else 0)

class card(object):
    def __init__(self, *b):
        if len(b)>0:
            self.value = b[0] #if a value is set
        else:
            self.value = -1 #indicates an unknown card

    def setValue(self, val):
        self.value = val
        return self

    def valueOnRack(self, rack, unavailableCards, availableCards):
        """
        returns the "goodness" of the card based on switching it with
        each card on rack and using ucards and acards for refernce.

        make sure this card is taken off of its previous list location before
        this function is called
        """
        #calculate goodness according to alg (use map)
        return map(goodness, [self for i in range(20)], rack, range(20))

    def statGoodness(self,rack):
        return .5
