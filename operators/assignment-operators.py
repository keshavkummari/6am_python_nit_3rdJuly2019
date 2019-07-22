# 3. Assignment Operators

"""
-------------------------------------------
Operator |	    Example	 |	Equivatent to
-------------------------------------------
1.   =			x = 5		x = 5
2.  +=			x += 5		x = x + 5	[+= Add AND]
3.  -=			x -= 5		x = x - 5	[-= Subtract AND]
4.  *=			x *= 5		x = x * 5	[*= Multiply AND]
5.  /=			x /= 5		x = x / 5	[/= Divide AND]
6.  %=			x %= 5		x = x % 5	[%= Modulus AND]
7.  //=			x //= 5		x = x // 5	[//= Floor Division]
8.  **=			x **= 5		x = x ** 5	[**= Exponent AND]
"""

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ",c, id(a),id(b),id(c),type(c))

c += a
print(f"Line-2 Value of C is {c}")

c -= a
print(f"Subtraction : {c}")

c *= a
print(f"Value of C is {c}")

c /= a
print(f"Division : {c}")

c = 1092
c //= a
print(f"Floor Division : {c}")

c = 2
c %= a
print(f"Modules : {c}")

c **= a
print(f"Exponent : {c}")