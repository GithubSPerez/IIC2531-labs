from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf



def login(username, password):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('login', username = username, password = password)
        return ret


def register(username, password):
    p_db = person_setup()
    person = p_db.query(Person).get(username)
    if person:
        return None
    
    newperson = Person()
    
    newperson.username = username
    
    

    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('register', username = username, password = password)
    
    if not (ret is None):
        p_db.add(newperson)
        p_db.commit()
        return ret
    
    return None

def check_token(username, token):
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as c:
        ret = c.call('check_token', username = username, token = token)
        return c.call('check_token', username = username, token = token)
