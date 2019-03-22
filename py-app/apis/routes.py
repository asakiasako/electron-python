from .modules.example import ROUTES as example

# Root path: ":"
API_ROUTES = {
    'method': None,
    'children': {
        'example': example
    }
}
