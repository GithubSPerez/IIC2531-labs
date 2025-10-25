from zoodb import *
from debug import *

import hashlib
import random

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput.encode('utf-8')).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == password:
        return newtoken(db, cred)
    else:
        return None

def register(username, password):
    c_db = cred_setup()
    cred = c_db.query(Cred).get(username)
    if cred:
        return None

    newcred = Cred()

    newcred.username = username
    newcred.password = password
    
    c_db.add(newcred)
    c_db.commit()

    return newtoken(c_db, newcred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

    
