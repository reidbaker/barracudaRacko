from SimpleXMLRPCServer import SimpleXMLRPCServer
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)
server = SimpleXMLRPCServer(('172.16.89.213', 80), logRequests=True)
# Expose a function
def list_contents(dir_name):
    logging.debug('list_contents(%s)', dir_name)
    return os.listdir(dir_name)


def ping(message):
    if message=='ping':
        return 'pong'
    else:
        return ''
    
server.register_function(ping)

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'