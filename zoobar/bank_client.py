from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def server():
    host = readconf.read_conf().lookup_host('bank')
    return rpclib.client_connect(host)

def register(username):
    return server().call('register', username = username)

def transfer(sender, recipient, zoobars):
    return server().call('transfer', sender = sender, recipient = recipient, zoobars = zoobars)

def balance(username):
    return server().call('balance', username = username)

def get_log(username):
    return server().call('get_log', username = username)



