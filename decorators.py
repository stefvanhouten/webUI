def auth(f):
    """ Decorator that checks if the machine returned any errors."""
    def wrapper(*args, **kwargs):
        headers = request.headers
        auth = headers.get("API_KEY")
        if auth != api_token:
            return jsonify({"errors": "Not authorized"})
        else:
            f(*args, **kwargs)
    return wrapper
