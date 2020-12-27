from hashlib import sha256

def update_hash(*args):
    hashing_text = ""; h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode("utf-8"))
    return h.hexdigest()

print(update_hash("hello"))

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


class Blockchain():
    pass


def main():
    block_1 = Block("My name is Matthew Williams", 25)


if __name__ == "__main__":
    main()