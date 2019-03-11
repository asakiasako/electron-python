
import multiprocessing
from server import rpc_server
from logger import rpcServerLogger
from sys import argv, stdout
import time
import threading


def flush_stdout_loop():
    while True:
        time.sleep(1)
        stdout.flush()


if __name__ == '__main__':
    # support freeze in exe
    multiprocessing.freeze_support()
    # log error and re-raise it
    t_flush_stdout = threading.Thread(target=flush_stdout_loop, daemon=True)
    t_flush_stdout.start()
    try:
        if len(argv) > 2:
            raise TypeError('Takes 1 argument but %d is given.' % len(argv))
        elif len(argv) == 2:
            port = int(argv[1])
            rpc_server(port)
        else:
            rpc_server()
    except Exception as e:
        rpcServerLogger.exception('RPC Server ERROR')
        raise e