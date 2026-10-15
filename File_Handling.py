import os
from pathlib import Path




# r = Read
# a = Append
# w = Write
# x = Create

# =================================================================================================

# Read - error if it doesnt exist


f = open("nama.txt") # r is optional


print(f.read())