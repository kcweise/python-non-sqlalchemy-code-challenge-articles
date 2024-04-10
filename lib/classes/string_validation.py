
def val_string(attr, value, min_len=None, max_len=None):
    if not isinstance(value, str):
        raise Exception(f"{attr} needs to be a string.")
    if min_len is not None and len(value)< min_len:
        raise Exception(f"{attr} must have at least {min_len} characters.")
    if max_len is not None and len(value)> max_len:
        raise Exception(f"{attr} must have no more than {max_len} characters.")