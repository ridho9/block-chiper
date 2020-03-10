from keygen import KeyGenerator

class Chiper():
    def init(self, key, ROUNDS=8):
        self.BLOCK_SIZE = 256
        self.ROUNDS = ROUNDS

        self.key = key
        self.keygen = KeyGenerator(key)
        self._gen_keys()
    
    def _transform(self, block, key):
        """
        Internal transformation function.
        """
        # TODO: implement the confusing part here
        return block

    def _split(self, block):
        """
        This function is used to split `block` into L and R for feistel network.
        """
        # TODO: mager
        L = block
        R = block
        return L, R
    
    def _merge(self, L, R):
        """
        This function is used to merge L and R from feistel network into a block.
        Should reversible from `Chiper.split()`
        """
        # TODO: mager
        block = (L << 32) + R
        return block
    
    def _gen_keys(self):
        # Generated the keys used for process.
        self.keys = [] 
        for r in range(self.ROUNDS):
            self.keys.append(self.keygen.next_key())
    
    def encode_block(self, block):
        next_L, next_R = self._split(block)

        for round in range(self.ROUNDS):
            prev_L, prev_R = next_L, next_R
            current_key = self.keys[round]

            next_L = prev_R
            next_R = prev_L ^ self._transform(prev_R, current_key)
        
        return self._merge(next_L, next_R)
    
    def decode_block(self, block):
        prev_L, prev_R = self._split(block)

        for round in reversed(range(self.ROUNDS)):
            next_L, next_R = prev_L, prev_R
            current_key = self.keys[round]

            prev_R = next_L
            prev_L = next_R ^ self._transform(next_L, current_key)
        
        return self._merge(prev_L, prev_R)
