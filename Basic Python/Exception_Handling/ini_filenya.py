# try       lets you test a block of code for errors.
# except    lets you handle the error.
# else      lets you execute code when there is no error.
# finally   lets you execute code, regardless of the result of the try- and except blocks.
# raise     To throw (or raise) an exception

### These occur while the program is running due to flawed data inputs, mismatched types, or invalid operations
# AttributeError	        An attribute reference or assignment fails on an object.
# IndexError	            A sequence (list, tuple, string) index is out of range.
# KeyError	                A dictionary key is not found.
# NameError	                A local or global variable name is not defined.
# TypeError	                An operation or function is applied to an inappropriate data type.
# ValueError	            A function receives an argument of the right type but an inappropriate value.
# ZeroDivisionError	        The second argument of a division or modulo operation is zero.
# AssertionError	        An assert statement fails.
# UnboundLocalError	        A reference is made to a local variable before it has been assigned a value.
# Exception                 Catch all exception

### These prevent the Python interpreter from parsing and running the script at al
# SyntaxError           Raised when the interpreter encounters invalid Python code structure.
# IndentationError      Incorrect spacing or alignment of code blocks

while True:
    try:
        n = int(input("Enter a number: "))
        print(2 / n)
        break
    except ZeroDivisionError:
        print("Cant divide by zero")
    except ValueError:
        print("can only enter a number")
    finally:
        print("test sudah berjalan")

