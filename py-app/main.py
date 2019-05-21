
import multiprocessing
from sys import argv, stdout, stderr
import time
import threading


def flush_stdio_loop():
    while True:
        time.sleep(1)
        stdout.flush()
        stderr.flush()

t_flush_stdout = threading.Thread(target=flush_stdio_loop, daemon=True)
t_flush_stdout.start()


if __name__ == '__main__':
    # support freeze in exe
    multiprocessing.freeze_support()
    try:
        if len(argv) > 3:
            raise TypeError('Takes 2 argument but %d is given.' % (len(argv)-1))
        elif len(argv) == 3:
            port = int(argv[1])
            user_data_path = argv[2]
            from paths import generate_sub_dirs
            generate_sub_dirs(user_data_path)
            from server import rpc_server
            from logger import rpcServerLogger
            rpc_server(port)
        else:
            rpc_server()
    except Exception as e:
        # log error and re-raise it
        rpcServerLogger.exception('RPC Server ERROR')
        raise e
