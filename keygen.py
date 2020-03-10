from lib import xorblock, rol

class KeyGenerator:
    def __init__(self, initial_key):
        self.initial_key = initial_key
    
    def gen(self):
        round = 0
        keylen = len(self.initial_key)
        lkey = self.initial_key[:keylen // 2]
        rkey = self.initial_key[keylen // 2 :]
        prevkey = lkey

        while True:
            rside = rol(rkey, (7*round) % 64)
            prevkey = xorblock(prevkey, rside)
            # print(f"{round=} {rside=} {prevkey=}")

            yield prevkey
            round += 1
    
if __name__ == "__main__":
    gen = KeyGenerator(b'12345678abcdefgh').gen()

    for _ in range(128):
        print(next(gen))
