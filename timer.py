import time

class timer(object):
    def __init__(self):
        self.t = 0
        self.startt = time.time()

    def time(self):
        self.t = time.time()-self.startt
        return .5 #self.t #for now it always returns time as not being up
