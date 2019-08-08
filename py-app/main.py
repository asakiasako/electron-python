import multiprocessing
import sys
import os

from paths import get_sub_dir
from logger import register_logger, get_logger


# disable stdout & stderr when frozen
if getattr(sys, 'frozen', False):
    # running in a bundle (mean frozen)
    # if frozen, disable child process stdio, otherwise stdio buffer may exceed
    # maxBuffer of node.js execFile, and this child process would be killed.
    f_nul = open(os.devnull, 'w')
    sys.stdout = f_nul
    sys.stderr = f_nul
else:
    import time
    import threading

    # if not frozen, flush stdio
    def flush_stdio_loop():
        while True:
            time.sleep(1)
            sys.stdout.flush()
            sys.stderr.flush()

    t_flush_stdout = threading.Thread(target=flush_stdio_loop, daemon=True)
    t_flush_stdout.start()


# register rpcServerLogger
rpcServerLogger = register_logger('RPCServer', os.path.join(get_sub_dir('Logs'), 'RPC-Server.log'))


if __name__ == '__main__':
    # support freeze in exe
    multiprocessing.freeze_support()

    try:
        # run RPCServer
        port = int(os.environ['rpcServerPort'])
        from server import rpc_server
        rpc_server(port)

    except Exception as e:
        # If error in main loop, log to file and re-raise.
        rpcServerLogger.exception('RPC Server ERROR')
        raise e
