#print('hello abhijit')
#print (10+10.3)
#course = 'Python for Pabflo'
#num = input("Enter the Table Number: ")
#for i in range(1, 11):
 #print (num, " * ", i , "=" , int(num) * i)

#name = input ('whats your name? ')
#color = input ('which is your fav color ' + name + ' ? ')
#print (name + ' likes '+ color)
#print (45888888888888888//7)
'''started=False
while True:
 command=input(">> ").lower()
 if command=="start":
  if started:
   print('car is already started')
  else:
   print("car started...")
  started=True
 elif command=="stop":
  if not started:
   print("car is already stopped")
  else:
   print("car is stopped")
  started=False
 elif command=="quit":
  print("game finished")
  break
 else:
  print('pls type correct command')'''

"""course='Juniperisagoodcompany'
new=(course[-7:2:-1])
print(new)"""
'''items=[2, 2, 2, 2, 11]
for item in items:
 output=''
 for i in range(item):
  output = output+'XX'
 print (output)'''

''' Finding digital sum 
num = int(input("Enter any number: "))
#print (len(num))
digi_sum=0
while num >0:
 rem=num%10
 num=num//10
 digi_sum=digi_sum+rem
if digi_sum%9==0:
  print ('digital sum is 9')
else:
  print(f'digital sum is {digi_sum%9}')'''

# Program to check if a number is prime or not

#num = 1061

# To take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
'''if num > 1:
 # check for factors
 for i in range(2, num//2):
  if (num % i) == 0:
   print(num, "is not a prime number")
   print(i, "times", num // i, "is", num)
   break
 else:
  print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
 print(num, "is not a prime number")'''
#To check if a number is palyndrome
'''num = int(input("Enter any number: "))
tmp=num
rev_digit=0
while num>0:
 digit=num%10
 num=num//10
 rev_digit=rev_digit*10+digit
 print(rev_digit)
 print(num)
if tmp == rev_digit:
 print(f'{tmp} is palindrome')
else:
 print(f'{tmp} is NOT palindrome')'''

#Find factorial of a positive number
'''num = int(input("Enter any number: "))
factorial_num=1
if num==0:
 print("factorial of 0 is 1")
#break
else:
 for i in range(1,num+1):
   factorial_num=factorial_num*i
 print(f'factorial of {num} is {factorial_num}')'''
#Another way of finding digital sum with string conversion method
'''num=input("Enter number: ")
sum=0
for i in num:
    sum = sum + int(i)
if sum%9 == 0:
    print (f'digital sum of {num} is 9')
else:
    print(f'digital sumo of {num} is {sum%9}')'''

#Print Fibonacci series for a number
'''num=int(input("Enter number : "))
fibo = 0
f1=0
f2=1
for i in range(0, num):
    print(f2, end = " ")
    fn=f1+f2
    f1=f2
    f2=fn'''
#Find square root of a number
'''num=int(input("enter number: "))
sqrt_num = num ** 0.5
print (sqrt_num)'''

#find decimal
'''name='abcdef'
dec=int(input("Enter decimal: "))
tmp=''
while (dec)>0:
    tmp=tmp+ str(dec%2)
    dec=dec//2
print (tmp[::-1], end='')'''
#num=int(input("Enter any number: "))

'''for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==0 or j==num-1 or i==j or (i+j)==num-1 or j==(num-1)//2 or i==(num-1)//2:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()'''
#Print S
'''for i in range(num):
        for j in range(num):
            if i==0 or i==num-1 or i==(num-1)//2:
              print('*', end=' ')
            elif i < (num - 1) // 2 and j==0:
              print('*', end=' ')
            elif i>(num-1)//2 and j==num-1:

              print('*', end=' ')
            else:
              print(' ', end=' ')
        print()

#Print O
for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==0 or j==num-1:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()
#Print N
for i in range(num):
    for j in range(num):
        if j==0 or j==num-1 or i==j:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()

#Print A

for i in range(num):
    for j in range(num):
        if (j==0 and i%3!=0) or i+j==num+1 or j-i==(num-1):
            print('*', end=' ')

        else:
            print(' ',end=' ')
    print()

#Print L

for i in range(num):
    for j in range(num):
        if i==num-1 or j==0:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()

#Print I
for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==(num-1)//2:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()'''


#Print solid Right Angle Triangle
'''for i in range(num):
    for j in range(i+1):

            print('*', end=' ')

    print()'''

#Print Hollow Right angle triangle

'''for i in range(num):
     for j in range(num):
         if j==0 or i==num-1 or j==i:
             print('*', end=' ')
         else:
             print(' ',end=' ')
     print()'''









#print right angle triangle with digits
'''for i in range(num):
    for j in range(i):

            print(j+1, end=' ')


    print()

for i in range(num):
    for j in range(num-i):
        print (j+1, end=' ')
    print()'''

#print equilateral triangle or pyramid shaped solid triangle
'''for i in range(num):
    for j in range(num-i-1):

        print(end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()'''

#print right angle triangle with character A, B etc
'''x=65
for i in range(num):
    #x=65
    for j in range(i+1):
        #x=65
        ch=chr(x)
        print(ch, end=' ')
        #x=x+1
    print()
    x=x+1'''
#print D
'''for i in range(num):
    for j in range(num):
        if j==0 or ((j==num-1) and (i!=0 and i!=num-1)) or ((i==0 or i==num-1) and (j>0 and j<num-1)):
            print('*', end='')
        else:
            print(end=' ')
    print()'''




# Enter number of terms needed                   #0,1,1,2,3,5....
a=int(input("Enter the terms"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print(f"The requested series is {f}")
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s
        print(next,end=" ")
        f=s
        s=next










