import os
from elevate import elevate


def is_root():
    return os.getpid() == 0

print("before ", is_root())
elevate()
print("after ", is_root())