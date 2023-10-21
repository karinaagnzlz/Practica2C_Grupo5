import os


def get_env(name, default=None, allow_false=False):
    """
    Quick access to os.environ.get
    """
    value = os.environ.get(name, default)
    if not (allow_false or value):
        return default
    return os.environ.get(name, default)


def bool_from_str(data):
    """
    Make  bool from string
    """
    if data is not None:
        dd = data.lower()
        if dd in ['false', 'f', 'n']:
            return False
        if dd in ['true', 't', 'y', 's']:
            return True
    return None
