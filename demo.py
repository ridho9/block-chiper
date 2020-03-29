from chiper import Chiper
from mode_operation import ModeOperation

pt1 = open("test/test256b", "rb").read()
pt2 = open("test/test12kb", "rb").read()

cipher = Chiper(b"1234567890abcdef")

pt = b"abcdefghijklmno"

print("Pesan Pendek")

operation = ModeOperation(cipher, ModeOperation.MODE_ECB)
ct = operation.encrypt(pt)
print("Ciphertext : ", ct.hex())
print()

pt = operation.decrypt(ct)
print("Plaintext : ", pt.hex())
print()

print("Pesan Sedang")

operation = ModeOperation(cipher, ModeOperation.MODE_ECB)
ct = operation.encrypt(pt1)
print("Ciphertext : ", ct.hex())
print()

pt = operation.decrypt(ct)
print("Plaintext : ", pt.hex())
print()
