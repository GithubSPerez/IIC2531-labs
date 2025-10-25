#!/usr/bin/env python3

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
    def rpc_register(self, username, password):
        #return None
        ret = auth.register(username, password)
        return ret
    
    def rpc_login(self, username, password):
        ret = auth.login(username, password)
        return ret

    def rpc_check_token(self, username, token):
        ret = auth.check_token(username, token)
        return ret

if len(sys.argv) != 2:
    print(sys.argv[0], "too few args")

s = AuthRpcServer()
s.run_fork(sys.argv[1])


