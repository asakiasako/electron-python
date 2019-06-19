import multiprocessing
from sys import argv
from logger import rpcServerLogger


if __name__ == '__main__':
    # support freeze in exe
    multiprocessing.freeze_support()

    if len(argv) == 1:
        port = 23300
    elif len(argv) != 2:
        raise TypeError('Takes 1 argument but %d is given.' % (len(argv)-1))
    else:
        port = int(argv[1])

    try:
        from server import rpc_server
        rpc_server(port)
    except Exception as e:
        # log error and re-raise it
        rpcServerLogger.exception('RPC Server ERROR')
        raise e
