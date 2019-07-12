"""
# String Special Operators:
                                 0 1 2 3 4 # Left to Right index
								-5-4-3-2-1 # Right to Left index
Assume string variable a holds ' H e l l o' and variable b holds 'Python', then :

Operator    : +
Description : Concatenation - Adds values on either side of the operator
Example     : a + b will give HelloPython

Operator    : *
Description : Repetition - Creates new strings,
              concatenating multiple copies of the same string
Example     : a*2 will give -HelloHello

Operator    : []
Description : Slice - Gives the character from the given index
Example     : a[1] will give e

Operator    : [ : ]
Description : Range Slice - Gives the characters from the given range
Example     :   a[1:4] will give ell

Operator    : [ : : ]
Description : Zero Based Indexing

Operator    :  %
Description :  Format - Performs String formatting
********************************************************************
# String Formatting Operator :
One of Pythons coolest features is the string format operator %.

This operator is unique to strings and makes up for the pack of having functions
from C's printf() family.

Below are the list of complete set of symbols which can be used along with % :

Format Symbol	Conversion
%c 				character
%s 				string conversion via str()
                                prior to formatting
%i 				signed decimal integer
%d 				signed decimal integer
%u 				unsigned decimal integer
%o 				octal integer
%x 				hexadecimal integer (lowercase letters)
%X 				hexadecimal integer (UPPERcase letters)
%e 				exponential notation (with lowercase 'e')
%E 				exponential notation (with UPPERcase 'E')
%f 				floating point real number
%g 				the shorter of %f and %e
%G 				the shorter of %f and %E


Operator    : r/R

Description : Raw String - Suppresses actual meaning of Escape characters.
The syntax for raw strings is exactly the same as for normal strings with
the exception of the raw string operator, the letter "r,"
which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and
must be placed immediately preceding the first quote mark.

Example     : print r'\n' prints \n and print R'\n' prints \n

"""

#!/usr/bin/python
       #01234567891011
       #-11-10-9-8-7-6-5-4-3-2-1
str1 = "Hello World!"  # 11 characters
str2 = 'This is an example string'

alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
          #A C E G I K M O Q S U W Y
          #0 2 4 6 8 10

"""
print (str1[0])
print (str1[-1])   # start index : end index -1 :
print (str1[2:6])  # 2:6 6-1 =5
print (str1[:5])
print (str1 * 3)

print(alphabets[0::2])

print("Updating String",str1[:6] + "Planet")

print(f"Updating String {str1[:6]} Planet")

name = "Guido Van Rossum"
account_number = 10203040

print("Your Name is %s and Your Account Number is %d" %(name,account_number))
print("Your Name is %s and Your Account Number is %d" %("Keshav",1020))
"""


para_str = r"""this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print (para_str)

para_str1 = R'''this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
'''
print (para_str1)
