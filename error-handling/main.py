
"""
try:
    something that might cause an exception/error
    
except:
    do this if there IS an exception

else:
    do this if there were no exceptions

finally:
    do this no matter what happens

raise:
    raise our own exceptions

"""

# File Not found
try:
    file = open("missing_file.txt") # FileNotFound Error
    a_dict = {"key": "value"}
    print(a_dict["key"]) # FIXED Key Error

# don't use bare except clause, it'll ignore all errors
# this was key error is still shown in terminal
except FileNotFoundError:
    # if doesn't exist, create it
    open("missing_file.txt", "w")

# to access error message for KeyError
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

# if try block was successful and no errors
else:
    content = file.read()
    print(content)

# finally, executed no matter what, can raise exception, use your own message
finally:
    raise TypeError("I made this error up")


