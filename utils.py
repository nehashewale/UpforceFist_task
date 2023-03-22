import logging
from functools import wraps

from flask import request, current_app as app
import flask_restful  


def sanitize_response(response):
    data = None
    status = 200
    headers = {}

    if isinstance(response, tuple) and len(response) is 3:
        (data, status, headers) = response
    if isinstance(response, tuple) and len(response) is 5:
        (status, data, code, message, header) = response
        return status, data, code, message, headers.update(header)
    else:
        data = response

    return (data, status, headers)

def patch_response_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response =  sanitize_response(func(*args,**kwargs))
        if isinstance(response,tuple) and len(response) is 5:
            status, data, code, message, headers = response

            data ={
                   "responseData": data,
                   "status": status,
                   "message": message
                   }
            
            return data, code, headers
        else:
            data, status, headers = sanitize_response(func(*args, **kwargs))
        
        patched = isinstance(data, dict) and (
            "errorCode" in data or "responseData" in data
        )

        if not patched:
            data = {
                "responseData": data
            }

        if 'errorCode' in list(data.keys()):
            status = data['errorCode']

        return (data, status, headers)
    return wrapper


class Resource(flask_restful.Resource):
    def options(self, **kwargs):
        logging.info("Obtained options request from %s",
                        request.remote_addr)
        return True, {}, 200, "OK", {'Content-Type':'application/json'}

    method_decorators = [
        patch_response_data
    ]

error_code_mapping = {200: "OK",
                      400: "BAD_REQUEST",
                      401: "UNAUTHORISED",
                      404: "NOT_FOUND",
                      500: "INTERNAL_SERVER_ERROR"
                      }

headers_mapping = {'csv': {'content-type':'application/csv'},
                   'json': {'content-type':'application/json'}}


def ok_response(response, message="OK", headers='json', status=True):
    return status, response, 200, message, headers_mapping['json']


def error_response(code, message, headers='json', status=False):
    response = {}
    return status, response, code, message, headers_mapping['json']
