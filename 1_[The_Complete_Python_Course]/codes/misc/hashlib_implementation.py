import hashlib

str1 = b"123pass"

sha256 = hashlib.sha256()

sha256.update(str1)

string_hash = sha256.hexdigest()


print(f"Hash:{string_hash}")
