# Ugly number verification
ugly_num=int(input("Enter the number:"))
if ugly_num%5==0 or ugly_num%3==0 or ugly_num%2==0:
    print("The given number is ugly number")
else:
    print("The given number is not a ugly number")
