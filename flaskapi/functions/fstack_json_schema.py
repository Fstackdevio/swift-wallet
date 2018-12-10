import json
from jsonschema import ValidationError, exceptions
from jsonschema.validators import Draft3Validator

from functools import wraps

from flask import _request_ctx_stack, request, jsonify

def _validate(schema, data):
    reqv = Draft3Validator(schema)
    errors = []
    for e in reqv.iter_errors(data):
        errors.append(dict(name=e.path[0], reason=e.validator))
    return errors

def validate(method, schema):
    def decorator(f):
        @wraps(f)
        def decorated_func(*args, **kws):
            ctype = request.headers.get("Content-Type")
            method_ = request.headers.get("X-HTTP-Method-Override", request.method)
            if method_.lower() == method.lower() and "json" in ctype:
                data = json.loads(request.data)
                errors = _validate(schema, data)
                if len(errors) > 0:
                    resp = jsonify(result="failure", reason="invalid json", errors=errors)
                    resp.status_code = 400
                    return resp
            return f(*args, **kws)
        return decorated_func
    return decorator
