from flask import request, jsonify

valid_tokens = ["valid_token_123"]

def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token not in valid_tokens:
            return jsonify({"message": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorator
