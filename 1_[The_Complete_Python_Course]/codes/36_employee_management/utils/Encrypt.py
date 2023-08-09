import hashlib

class Encrypt:
    def check_password(self, password, db_pass):

        string_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if string_hash == db_pass:
            return True
        else:
            return False



if __name__ == "__main__":
    encrypt = Encrypt()
    encrypt.check_password("pass123", "9b8769a4a742959a2d0298c36fb70623f2dfacda8436237df08d8dfd5b37374c")