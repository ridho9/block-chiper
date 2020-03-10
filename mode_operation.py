from chiper import *


class ModeOperation:
    MODE_ECB = 0
    MODE_CBC = 1
    MODE_CFB = 2
    MODE_OFB = 3
    MODE_COUNTER = 4

    def __init__(self, cipher: Chiper, mode, iv=None, counter=0):
        self.mode = mode
        self.cipher = cipher
        self.BLOCK_SIZE = cipher.BLOCK_SIZE
        self.iv = b"" * self.BLOCK_SIZE if iv is None else iv
        self.counter = counter

    @staticmethod
    def _xorblock(b1, b2):
        return bytes(a ^ b for (a, b) in zip(b1, b2))

    def _encrypt_ecb(self, block_plaintext):
        ciphertext = b""
        for block in block_plaintext:
            ciphertext += self.cipher.encode_block(block)
        return ciphertext

    def _encrypt_cbc(self, block_plaintext):
        ciphertext = b""
        prev_block = self.iv
        for block in block_plaintext:
            result = self.cipher.encode_block(ModeOperation._xorblock(prev_block, block))
            prev_block = result
            ciphertext += result
        return ciphertext

    def _encrypt_cfb(self, block_plaintext):
        ciphertext = b""
        prev_block = self.iv
        for block in block_plaintext:
            result = self.cipher.encode_block(prev_block)
            prev_block = ModeOperation._xorblock(result, block)
            ciphertext += prev_block
        return ciphertext

    def _encrypt_ofb(self, block_plaintext):
        ciphertext = b""
        prev_block = self.iv
        for block in block_plaintext:
            result = self.cipher.encode_block(prev_block)
            prev_block = result
            ciphertext += ModeOperation._xorblock(result, block)
        return ciphertext

    def _encrypt_counter(self, block_plaintext):
        ciphertext = b""
        counter: int = self.counter
        for block in block_plaintext:
            block_counter = counter.to_bytes(self.BLOCK_SIZE / 8, "big")
            result = self.cipher.encode_block(block_counter)
            ciphertext += ModeOperation._xorblock(result, block)
            counter += 1
        return ciphertext

    def encrypt(self, plaintext):
        if len(plaintext) % self.BLOCK_SIZE != 0:
            raise Exception("Invalid size plaintext")

        n = self.BLOCK_SIZE
        block_plaintext = [plaintext[n*i:n*(i+1)] for i in range(len(plaintext) / n)]

        if self.mode == ModeOperation.MODE_ECB:
            return self._encrypt_ecb(block_plaintext)
        elif self.mode == ModeOperation.MODE_CBC:
            return self._encrypt_ecb(block_plaintext)
        elif self.mode == ModeOperation.MODE_CFB:
            return self._encrypt_ecb(block_plaintext)
        elif self.mode == ModeOperation.MODE_OFB:
            return self._encrypt_ecb(block_plaintext)
        elif self.mode == ModeOperation.MODE_COUNTER:
            return self._encrypt_ecb(block_plaintext)

    def _decrypt_ecb(self, block_ciphertext):
        plaintext = b""
        for block in block_ciphertext:
            plaintext += self.cipher.decode_block(block)
        return plaintext

    def _decrypt_cbc(self, block_ciphertext):
        plaintext = b""
        prev_block = self.iv
        for block in block_ciphertext:
            result = self.cipher.decode_block(block)
            plaintext += ModeOperation._xorblock(result, prev_block)
            prev_block = block
        return plaintext

    def _decrypt_cfb(self, block_ciphertext):
        plaintext = b""
        prev_block = self.iv
        for block in block_ciphertext:
            result = self.cipher.decode_block(prev_block)
            plaintext += ModeOperation._xorblock(result, block)
            prev_block = block
        return plaintext

    def _decrypt_ofb(self, block_ciphertext):
        plaintext = b""
        prev_block = self.iv
        for block in block_ciphertext:
            result = self.cipher.decode_block(prev_block)
            prev_block = result
            plaintext += ModeOperation._xorblock(result, block)
        return plaintext

    def _decrypt_counter(self, block_ciphertext):
        plaintext = b""
        counter: int = self.counter
        for block in block_ciphertext:
            block_counter = counter.to_bytes(self.BLOCK_SIZE / 8, "big")
            result = self.cipher.decode_block(block_counter)
            plaintext += ModeOperation._xorblock(result, block)
            counter += 1
        return plaintext

    def decrypt(self, ciphertext):
        if len(ciphertext) % self.BLOCK_SIZE != 0:
            raise Exception("Invalid size ciphertext")

        n = self.BLOCK_SIZE
        block_ciphertext = [ciphertext[n*i:n*(i+1)] for i in range(len(ciphertext) / n)]

        if self.mode == ModeOperation.MODE_ECB:
            return self._decrypt_ecb(block_ciphertext)
        elif self.mode == ModeOperation.MODE_CBC:
            return self._decrypt_ecb(block_ciphertext)
        elif self.mode == ModeOperation.MODE_CFB:
            return self._decrypt_ecb(block_ciphertext)
        elif self.mode == ModeOperation.MODE_OFB:
            return self._decrypt_ecb(block_ciphertext)
        elif self.mode == ModeOperation.MODE_COUNTER:
            return self._decrypt_ecb(block_ciphertext)
