"""
An entry for all zeroRPC APIs
Specified apis are classed in package api
This is the entry of the entire python app
"""

from .configs import *
import time
import traceback
import zerorpc
from apis import API


def parse_addr(port=23300):
    """
    RPC server config
    :param local: (bool) start a local server or not.
    :param port: (int) server port
    :return: (str) parsed address like: 'tcp://0.0.0.0:4321'
    """
    ip = '127.0.0.1'
    if not isinstance(port, int):
        raise TypeError('port shall be int.')
    addr = 'tcp://%s:%d' % (ip, port)
    return addr


def rpc_server(port=DEFAULT_SERVER_PORT):
    """
    Start RPC server, and serve APIs in class API
    :return:
    """
    addr = parse_addr(port=port)
    server = zerorpc.Server(API())
    server.bind(addr)
    info_str = '\n------------------------------------------\n\n RPC server started on: %s\n\n------------------------------------------\n' % addr
    print(info_str)
    server.run()
