from .routes import API_ROUTES
from logger import get_logger


rpcServerLogger = get_logger('RPCServer')


class APIRouteError(Exception):
    def __init__(self, *args, **kwargs):
        super(APIRouteError, self).__init__(*args, **kwargs)


def api_router(params):
    # unpack
    if not isinstance(params, dict):
        raise TypeError('Argument sent to request method should be a dict.')
    if 'route' not in params:
        raise KeyError('No "route" key found in request dict.')
    api_route_str = params['route']
    api_args = []
    api_kwargs = {}
    if not isinstance(api_route_str, str):
        raise TypeError('The value of key "args" should be a str')
    if not api_route_str.startswith(':'):
        raise ValueError('route should starts with ":"')
    if 'args' in params:
        api_args = params['args']
        if not isinstance(api_args, (tuple, list)):
            raise TypeError('The value of key "args" should be a tuple or list.')
    if 'kwargs' in params:
        api_kwargs = params['kwargs']
        if not isinstance(api_kwargs, dict):
            raise TypeError('The value of key "kwargs" should be a dict.')

    # route to target and get api method
    api_route_dir = api_route_str.strip().split(':')
    api_route_dir.pop(0)
    route_target = API_ROUTES

    try:
        for i in api_route_dir:
            if i != '':
                route_target = route_target['children'][i]
    except KeyError:
        raise APIRouteError('Route does not exist: "%s"' % api_route_str)
    
    try:
        api_method = route_target['method']
    except KeyError:
        raise APIRouteError('No method registered to route: "%s"' % api_route_str)
    else:
        if api_method is None:
            raise APIRouteError('No method registered to route: "%s"' % api_route_str)
    
    # run method and return
    return api_method(*api_args, **api_kwargs)


class API:
    @staticmethod
    def request(params):
        try:
            return api_router(params)
        except Exception as e:
            if 'route' in params:
                route = params['route']
            else:
                route = 'No route in request params.'
            rpcServerLogger.exception('API method error: "%s"' % route)
            raise e
    
    @staticmethod
    def check_connection():
        return True
