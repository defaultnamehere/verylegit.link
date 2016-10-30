import urllib
import base64

def firebase_escape(string):
    """'.$[]#/' are not valid Firebase key characters, so we have to 
    not store them before we can store the URL"""
    return base64.urlsafe_b64encode(string.encode("utf8"))

def firebase_unescape(string):
    return base64.urlsafe_b64decode(string.encode("utf8"))

def escape_string_args(func):
    def wrapper(*args, **kwargs):
        import ipdb; ipdb.set_trace()
        escaped_args = []
        escaped_kwargs = {}
        if args is not None:
            escaped_args = [firebase_escape(arg)
                            if isinstance(arg, str)
                            else arg
                            for arg in args]
        if kwargs is not None:
            escaped_kwargs = {
                key: firebase_escape(value) 
                if isinstance(value, str) 
                else value
                for key, value in kwargs.items()
            }
        return func(*escaped_args, **escaped_kwargs)
    return wrapper

def unescape_output(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        if isinstance(output, str):
            return firebase_unescape(output)
        return output

