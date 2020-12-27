from models.block import Block
from models.blockchain import Blockchain


def main():
    blockchain = Blockchain()
    database = ["Matt", "25", "hello"]

    num = 0
    for data in database:
        num += 1
        blockchain.mine(Block(data, num))

    print(blockchain.chain)
    for block in blockchain.chain:
        print(block)


if __name__ == "__main__":
    main()