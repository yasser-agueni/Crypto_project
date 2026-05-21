import hashlib


def sha1(message):

    return hashlib.sha1(
        message.encode()
    ).hexdigest()



def sha256(message):

    return hashlib.sha256(
        message.encode()
    ).hexdigest()

