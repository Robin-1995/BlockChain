import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data=None, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()

        hash_str = str(data).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        current_time = datetime.datetime.utcnow()
        if self.head is None:
            self.head = Block(timestamp=current_time, data=data)
            self.length += 1
            return
        block = self.head
        while block.next:
            block = block.next

        block.next = Block(timestamp=current_time, data=data, previous_hash=block.hash)
        self.length += 1

        return

    def to_list(self):

        if self.length == 0:
            print("Blockchain is empty, nothing to print. Try appending some blocks to the chain")
            return
        out = []
        block = self.head
        while block:
            out.append([block.timestamp, block.data, block.hash, block.previous_hash])
            block = block.next
        return out


# #Test 1 <-- print a list of each block in the chain, length = 10
# chain1 = BlockChain()
#
# for i in range(0,10):
#     chain1.append(i)
#
# print(chain1.to_list())
# print()
# print()
#
# # Test 2 <-- print statement and return None
# chain2 = BlockChain()
# print(chain2.to_list())
# print()
# print()
#
# # Test 3 <-- return a list of 1 block with the data value of 150
# chain3 = BlockChain()
# chain3.append(150)
# print(chain3.to_list())
# print()
# print()
#
# #Test 4 <-- print a list of each block in the chain , length = 30
# chain1 = BlockChain()
#
# for i in range(0,30):
#     chain1.append(i)
#
# print(chain1.to_list())
# print()
# print()