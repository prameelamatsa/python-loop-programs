num=int(input("enter any value:"))
p=1
while(num):
    r=num%10
    p=p*r
    num=num//10
    print("product of digit is ",p)
