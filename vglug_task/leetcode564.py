n=1
# if len(str(n)) != 1:
de_count=0
for i in range(n,0,-1):
    de_count+=1
    if str(i)==str(i)[::-1]:      
        dec1=de_count
        dec2=i
        break
inc_count=0
while True:
    inc_count+=1
    n+=1
    if str(n)==str(n)[::-1] :
        inc1=inc_count
        inc2=n
        break
if inc1==dec1:
    if inc1<dec1:
        print(dec1)
if inc1<dec1:
    print(inc2)
elif inc1>dec1:
    print(dec2)
else:
    print()
