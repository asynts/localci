import secrets

_abc = "abcdefghijklmnopqrstuvwxyz"
_ABC = _abc.upper()
_digits = "0123456789"

def passwd(pattern="aAdd-xxxx-xxxx-xxxx"):
    lambdas = {
        "a": lambda: secrets.choice(_abc),
        "A": lambda: secrets.choice(_ABC),
        "d": lambda: secrets.choice(_digits),
        "x": lambda: secrets.choice(_abc + _ABC + _digits),
        "-": lambda: "-"
    }

    return "".join(lambdas[placeholder]() for placeholder in pattern)

def email():
    identifier = secrets.randbelow(2 ** 64)
    return f"asynts+{identifier:016x}@gmail.com"
