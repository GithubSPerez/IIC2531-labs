#!/usr/bin/env python3

import rpclib
import sys
import bank
from debug import *

class BankRpcServer(rpclib.RpcServer):
    def rpc_register(self, username):
        ret = bank.register(username)
        return ret

    def rpc_transfer(self, sender, recipient, zoobars):
        #return None
        ret = bank.transfer(sender, recipient, zoobars)
        return ret
    
    def rpc_balance(self, username):
        ret = bank.balance(username)
        return ret

    def rpc_get_log(self, username):
        ret = bank.get_log(username)
        return ret

if len(sys.argv) != 2:
    print(sys.argv[0], "too few args")

s = BankRpcServer()
s.run_fork(sys.argv[1])


