from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def caller():
    host = readconf.read_conf().lookup_host('bank')
    return rpclib.client_connect(host)

def register(username):
    return caller().call('register', username = username)

def transfer(sender, recipient, zoobars):
    return caller().call('transfer', sender = sender, recipient = recipient, zoobars = zoobars)

def balance(username):
    return caller().call('balance', username = username)

def get_log(username):
    return caller().call('get_log', username = username)



