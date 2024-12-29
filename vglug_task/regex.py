import re
string="abc123abcskhci"
result1=re.match(r"abc",string)
result2=re.search(r"abc",string)
result3=re.findall(r"abc",string)
result4=re.finditer(r"abc",string)
print(result1)
print(result2)
print(result3)
for a in result4:
    print(a)

""" 
methods of regular expression
    1.match ( only consider beginning)
    2.search ( Search every corner)
    3.findall ( )
    4.finditer"""
