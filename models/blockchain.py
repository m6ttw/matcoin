class Blockchain():
    difficulty = 4

    def __init__(self, chain=[]):
        self.chain = chain

    def add(self, block):
        self.chain.append(
            {
            "hash": block.hash(),
            "previous_hash": block.previous_hash,
            "number": block.number,
            "data": block.data,
            "nonce": block.nonce
            }
        )

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].get("hash")
        except IndexError:
            pass

        while True:
            if block.hash()[:4] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nonce += 1
