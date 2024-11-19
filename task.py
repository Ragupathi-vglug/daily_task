# task one
price_list=input("Enter the list if three item price :").split()
#print(price_list)
a=int(price_list[0])
b=int(price_list[1])
c=int(price_list[2])

if a==b:
    a1=a-(10/a*100)
    b1=b-(10/b*100)
    d1=a1+b1+c
    print(d1)    

elif b==c:
    b1=b-(10/b*100)
    c1=c-(10/c*100)
    d2=sum(b1+c1+a)
    print(d2)
    
elif c==a:
    c1=c-(10/c*100)
    a1=a-(10/a*100)
    d3=c1+a1+b
    print(d3)

else:
    print("Your given items doesn't have any same price of two products")
