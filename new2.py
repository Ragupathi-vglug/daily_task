# m=100
# for a in range(1,m+1):
#     if m%a==0:
#         print(a)
m = 100
count = 0
while True:
    count+=1
    if m % count == 0:
        print(count)
    elif count == 101:
        break
