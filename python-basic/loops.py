#             ( Programs related to loops )
WAP print table of any number
n=int(input("Enter any number for get table:"))
for i in range(n,n*10+n,n):
    print(i)

# WAP calculation factrial value given of any number

n=int(input("Enter your number for get factorial :"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("Factorial is ",fact)

# WAP sum of all number from 1 to n given number
n=n=int(input("Enter your number :"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of all number from 1 to",n," :",sum)

# WAP sum of all even number from 1 to n given number 
n=int(input("Enter your number :"))
sum=0
for i in range(0,n+1,2):
    sum=sum+i
    print(i)
print("Sum of all even number from 1 to",n," :",sum)

# WAP sum of all number odd number from 1 to n given number
n=int(input("Enter your number :"))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
    print(i)
print("Sum of all even number from 1 to",n," :",sum)

# WAP sum of all given any 5 number
sum=0 
for i in range(5):
    num=int(input("Enter your number :"))
    sum=sum+num
print("Sum of your number is :",sum)



# WAP print all even number from 2 to 20 
i=0
sum=0
while i<=20:
    print(i)
    sum=sum+i
    i=i+2
print("Sum of even number from 1 to 20 :",sum)

# WAP print sum of all number from 1 to 20
i=1
sum=0
while i<=20:
    print(i)
    sum=sum+i
    i=i+1
print("Sum of number from 1 to 20 :",sum)

# WAP print all odd number fdrom 1 to 220
i=1
sum=0
while i<=220:
    print(i)
    sum=sum+i
    i=i+2
print("Sum of odd number from 1 to 220 :",sum)

# WAP print table of 5 
n=5
i=1
while i<=10:
    print(n,"X",i,"=",i*n)
    i+=1

# WAP print all even number in reverse format  from 80 to 20
i=80
while i>=20:
    print(i)
    i-=2

# WAP print all even number from 3to 18
i=3
while i<=18:
    print(i)
    i+=2


# WAP print all odd number from 50 to 5
i=50
while i>=5:
    if i%2==0:
        pass
    else:
        print(i)
    i-=1

# WAP sum of all even number from 5 to 30
i=5
while i<=50:
    if i%2==0:
        print(i)
    else:
       pass
    i+=1

# WAP sum of all odd number from 51 to 100
i=51
while i<=100:
    if i%2==0:
        pass
    else:
        print(i)
    i+=1

# WAP print all number from 1 to 100 which number is divide by 5
i=1
while i<=100:
    if i%5==0:
        print(i)
    else:
        pass
    i+=1




