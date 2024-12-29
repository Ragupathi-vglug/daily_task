import os
f=open("ragu.txt","r+")
print(f.write("hi"))
f.close()
f=open("ragu.txt","r")
print(f.read())

