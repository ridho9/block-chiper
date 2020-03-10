from chiper import Chiper
from mode_operation import ModeOperation
from time import time

pt1 = open("test/test256b", "rb").read()
pt2 = open("test/test12kb", "rb").read()

def do_benchmark(operation):
    print("256 bytes")
    start = time()
    c = operation.encrypt(pt1)
    end = time()
    print(f"Encrypt {end - start}")

    start = time()
    p = operation.decrypt(c)
    end = time()
    print(f"Decrypt {end - start}")

    assert p[:len(pt1)] == pt1

    print("12 kb")
    start = time()
    c = operation.encrypt(pt2)
    end = time()
    print(f"Encrypt {end - start}")

    start = time()
    p = operation.decrypt(c)
    end = time()
    print(f"Decrypt {end - start}")

    assert p[:len(pt2)] == pt2


cipher = Chiper(b"1234567890abcdef")

# ---------------------------------------------------------------------------------------------
print("ECB")
operation = ModeOperation(cipher, ModeOperation.MODE_ECB)
do_benchmark(operation)

# ---------------------------------------------------------------------------------------------
print("\nCBC")
operation = ModeOperation(cipher, ModeOperation.MODE_CBC, iv=b"qwertyuiopasdfgh")
do_benchmark(operation)

# ---------------------------------------------------------------------------------------------
print("\nCFB")
operation = ModeOperation(cipher, ModeOperation.MODE_CFB, iv=b"qwertyuiopasdfgh")
do_benchmark(operation)

# ---------------------------------------------------------------------------------------------
print("\nOFB")
operation = ModeOperation(cipher, ModeOperation.MODE_OFB, iv=b"qwertyuiopasdfgh")
do_benchmark(operation)

# ---------------------------------------------------------------------------------------------
print("\nCOUNTER")
operation = ModeOperation(cipher, ModeOperation.MODE_COUNTER, counter=0x1337)
do_benchmark(operation)

# ---------------------------------------------------------------------------------------------
print("ECB")
pt = b"Lorem ipsum dolor sit amet, consectetur adipisci"

operation = ModeOperation(cipher, ModeOperation.MODE_ECB)
ct = operation.encrypt(pt)
print(ct.hex())

cipher = Chiper(b"1234567890abcdeg")
operation = ModeOperation(cipher, ModeOperation.MODE_ECB)
ct = operation.encrypt(pt)
print(ct.hex())
