from SimpleXMLRPCServer import SimpleXMLRPCServer
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
    return ''



try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'