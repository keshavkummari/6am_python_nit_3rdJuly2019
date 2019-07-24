"""
You may need to process a function for more arguments than you specified while defining the function.
These arguments are called variable-length arguments and are not named
in the function definition,
unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is this :

Note: An asterisk (*) is placed before the variable name that
holds the values of all
nonkeyword variable arguments.

This tuple remains empty if no additional arguments are specified during the function call.


def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
"""
# Example -1:
# Function definition is here
def Test(*a):
   #This prints a variable passed arguments
   for var in a:
       print (var)

   return

# Now you can call printinfo function
#Test( 10 )

Test(10,20,30,40,50,60,70)
