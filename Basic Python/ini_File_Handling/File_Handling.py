
import os
from pathlib import Path




# r = Read
# a = Append
# w = Write
# x = Create

# =================================================================================================

# Read - error if it doesnt exist ---------------------------------------


#f = open("nama.txt",'r') # r is optional


#print(f.read(4))
#print(f.readline())

"""for x in f:
    print(x)"""

"""f.close()
try:
    f = open("file_ini_tidak_ada")
    print(f.read())
except:
    print("file ini tidak pernah ada")
finally:
    f.close()"""


# Append - creates the file id it doesnt exist ---------------------------------------


"""f = open("nama.txt",'a')
f.write("Mang usep")
f.close()


f = open("nama.txt")
f.read()
f.close()"""



# Write (Overwrite) ---------------------------------------


"""f = open("context.txt","w")
f.write("kamu kena hack")
f.close()"""




# Create a new files (2 way) ---------------------------------------

# Opens a file for writing, creates the file if it doesnt exist
"""f = open("nama_game.txt",'w')
f.close()
"""
# Creates the specified file, but retruns an error if it exist

if not os.path.exists("ngga.txt"): 
    print("eweh")
    f = open("ngga.txt",'x')
    f.close()
else:
    print("Filenya sudah ada")

# Delete a file
# avoid an error if it doesnt exist

"""if os.path.exists("ngga.txt"):
    os.remove("ngga.txt")
    print("FIle ngga.txt has been deleted")
else:
    print("Filenya tidak ada")"""


with open("ngga.txt") as f:
    content = f.read()

with open("nama.txt",'w') as f:
    f.write(content)
