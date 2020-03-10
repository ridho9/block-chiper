def xorblock(b1, b2):
    return bytes(a ^ b for (a, b) in zip(b1, b2))