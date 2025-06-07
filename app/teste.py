import hashlib


def hashing(dados):
    hash_object = hashlib.sha512()
    hash_object.update(dados.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex


print(hashing("fábio"))