'''
An else statement can be combined with an if statement.
An else statement contains the block of code that executes if the conditional expression
in the if statement resolves to 0 or a FALSE value.

The else statement is an optional statement and there could be
at most only one else statement following if .
'''

# Syntax :

"""
if expression:
   statement(s)
else:
   statement(s)
"""

# Creating a Variable in Python
course_name = "Python"

# Evaluate the Condition
if course_name.lower() == "python":     # : Suite
    print("Conditon is True")           # 4 whitespacess or one tab
else:
    print("Condition is False")

