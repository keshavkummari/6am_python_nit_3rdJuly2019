import re
# If we need the exact positions of each match
#regex = r"([a-zA-Z]+) \d+"

#matches = re.finditer(regex,'June 24, Aug 9, Dec 12') 
                                        # 0123456789
matches = re.finditer(r"([a-zA-Z]+) \d+",'June 24, Aug 9, Dec 12') 

for var_expression in matches:
    print("Match at Index : %s , %s" % (var_expression.start(),var_expression.end()))