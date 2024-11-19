cost=int(input("Enter the Rupees of denomination:"))

a=cost//5
b=cost-(a*5)
c=b//2
d=b-(c*2)
e=d
print(a,b,c,d)

print("Count of Rs.5:",a)
if c>0:
    print("Count of Rs.2:",c)
if e>0:
    print("Count of Rs.1:",e)


cost = int(input("Enter the Rupees of denomination:"))
a = cost // 5
b = cost - (a * 5)
c = b // 2
d = b - (c * 2)
print("Count of Rs.5:", a)
if c > 0:
    print("Count of Rs.2:", c)
if d > 0:
    print("Count of Rs.1:", d)