from chiper import Chiper
from mode_operation import ModeOperation

cipher = Chiper(b"1234567890abcdeg")
operation = ModeOperation(cipher, ModeOperation.MODE_CFB, iv=b"\x00" * 16)

o = operation.encrypt(b"1234567890abcdef1234567890abcdef1234567890abcdef")

print(o)

o = operation.decrypt(o)
print(o)