# Exception Handling with Try..except...else...finally

# Format-1
try:                    # The Try block lets you test a block of code for errors
    statement(s)
except:                 # The except block lets you handle the error
    statement(s)

# Format-2
try:
    statement(s)
except:
    statement(s)
except:
    statement(s)
except:
    statement(s)

# Format-3
try:
    statement(s)
except:
    statement(s)
except:
    statement(s)
except:
    statement(s)
else:         # Else is going to define a block of code to be executed if no errors were raised
    statement(s)

# Format-4
try:
    statement(s)
except:
    statement(s)
else:
    statement(s)
finally:
# The Finally block lets you execute code, regardless of the results of the try and except blocks
    statement(s)