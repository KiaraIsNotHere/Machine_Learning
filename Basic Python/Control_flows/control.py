import random
""""

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""

a = random.randrange(0,100)
b = random.randrange(0,100)

# Basic if elif else ------------------------------------------------------------------------------------------------

"""if int(a) < 0:
    print(f"Angka {a} ini bernilai negatif")
elif int(a) < 10:
    print(f"Angka {a} ini kurang dari 10")
elif int(a) < 50:
    print(f"Angka {a} ini kurang dari 50")
elif int(a) < 100:
    print(f"Angka {} ini kurang dari 100")
else:
    print(f"Angka {a} ini lebih dari 100")"""

# Shorthand ------------------------------------------------------------------------------------------------
print("A is BIGGER") if a > b else print("B is BIGGER ") 

x = "A is NIGGER than b" if a > b else "is equal" if a < b else print("B is NIGGER")


