
def sd(num):
        sum=0
        if num>0:
            n1=num%10
            return n1+sd(num//10)
        else:
            return 0
    num=int(input("Enter the number"))
    sd(num)