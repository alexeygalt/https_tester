import requests

METHODS = {'GET': requests.get, 'POST': requests.post, 'PUT': requests.put, 'DELETE': requests.delete,
           'HEAD': requests.head, 'PATCH': requests.patch, 'OPTIONS': requests.options}

