def xorblock(b1, b2):
    return bytes(a ^ b for (a, b) in zip(b1, b2))

def rol(block, n):
    v = int.from_bytes(block, 'big')
    res = (v << n) &  ((1 << 64) - 1)  | (v >> (64 - n))
    return res.to_bytes(8, 'big')