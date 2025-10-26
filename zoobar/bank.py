from zoodb import *
from debug import *

import time

def register(username):
    db = bank_setup()
    bank = db.query(Bank).get(username)
    if bank:
        return None
    
    newbank = Bank()
    newbank.username = username
    newbank.zoobars = 10

    db.add(newbank)
    db.commit()

    return True

def transfer(sender, recipient, zoobars):
    bankdb = bank_setup()

    sender_bank = bankdb.query(Bank).get(sender)
    recipient_bank = bankdb.query(Bank).get(recipient)

    sender_balance = sender_bank.zoobars - zoobars
    recipient_balance = recipient_bank.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    sender_bank.zoobars = sender_balance
    recipient_bank.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = bank_setup()
    bank = db.query(Bank).get(username)
    return bank.zoobars

def get_log(username):
    db = transfer_setup()
    l = db.query(Transfer).filter(or_(Transfer.sender==username,
                                      Transfer.recipient==username))
    r = []
    for t in l:
       r.append({'time': t.time,
                 'sender': t.sender ,
                 'recipient': t.recipient,
                 'amount': t.amount })
    return r 


