from hashlib import sha256
#'secure hash algorithm 256' - transforms data into indecipherable hash value

def update_hash(*args): #*args allows you to pass a varying number of positional arguments
    text_to_hash = ""; h = sha256()
    for arg in args:
        text_to_hash += str(arg)

    h.update(text_to_hash.encode("utf-8"))
    return h.hexdigest() #returns encoded data in hexadecimal format


class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return update_hash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )

    def __str__(self):
        return str(
            "Block#: %s\n" +
            "Hash#: %s\n" +
            "Previous#: %s\n" +
            "Data#: %s\n" +
            "Nonce#: %s\n" %(
                self.number,
                self.hash(),
                self.previous_hash,
                self.data,
                self.nonce
            )
        )
