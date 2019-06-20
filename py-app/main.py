import multiprocessing
import sys
import os


# disable stdout & stderr when frozen
if getattr(sys, 'frozen', False):
    # running in a bundle (mean frozen)
    # if frozen, disable child process stdio, otherwise stdio buffer may exceed
    # maxBuffer of node.js execFile, and this child process would be killed.
    f_nul = open(os.devnull, 'w')
    sys.stdout = f_nul
    sys.stderr = f_nul


from logger import rpcServerLogger

if __name__ == '__main__':
    # support freeze in exe
    multiprocessing.freeze_support()

    try:
        if len(sys.argv) == 1:
            port = 23300
        elif len(sys.argv) != 2:
            raise TypeError('Takes 1 argument but %d is given.' % (len(sys.argv)-1))
        else:
            port = int(sys.argv[1])
        # import & run rpc_server
        from server import rpc_server
        rpc_server(port)
    except Exception as e:
        # log error and re-raise it
        rpcServerLogger.exception('RPC Server ERROR')
        raise e
