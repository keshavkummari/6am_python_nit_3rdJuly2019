"""
3. The elif Statement :

The elif statement allows you to check multiple expressions for TRUE
and execute a block of code as soon as one of the conditions evaluates to TRUE.

Syntax:

if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)


"""

# Creating a Variable in Python
course_name = "Python"

# Evaluate the Condition
if course_name == "python":     # : Suite
    print("Conditon is True")           # 4 whitespacess or one tab
elif course_name == "PYTHON":
    print("I am a ELIF Block-I - Condition is TRUE")
elif course_name == "Python":
    print("I am a ELIF Block-II - Condition is TRUE")
else:
    print("Condition is False")
