'''myfile = open ("data.txt", "rt")
contents = myfile.read()         # read the entire file to string
myfile.close()                   # close the file
print(contents)'''

'''with open ('data.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:              # For each line, read to a string,
        print(myline)'''

'''mylines = []                                # Declare an empty list.
with open ('data.txt', 'rt') as myfile:    # Open lorem.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.strip('\n')) # strip newline and add to list.
                    # For each element in the list,
    #print(mylines[14])
    uuid=mylines[14]
    uuid_val=uuid.split(":")
    slb_srv_uuid=uuid_val[1].replace(',','').strip('\"')
    print(slb_srv_uuid)'''

#Add two binary numbers
'''c=0
r=''
s1=0
s2=0
s3=0
str1=input("enter 1st binary number ")
l1=len(str1)
str3=str1[::-1]

for p in range(l1):
    s1=s1+(int(str3[p])*(2**p))
print(s1)

str2=input("enter 1st binary number ")
str4=str2[::-1]
l1=len(str4)
for p in range(l1):
    s2=s2+(int(str4[p])*(2**p))
print(s2)
i=len(str1)-1
while(i>=0):
    if int(str1[i])+int(str2[i]) == 2:
        if c==1:
            r='1'+r
            c=1
        else:
            r='0'+r
            c=1
    elif int(str1[i]) + int(str2[i]) == 1:
        if c==1:
            r='0'+r
            c=1
        else:
            r='1'+r
            c=0
    elif int(str1[i]) + int(str2[i]) == 0:
        if c==1:
            r='1'+r
            c=0
        else:
            r='0'+r
            c=0

    i=i-1

print(r)
print(c)

if c==1:
    r='1'+r

str5=r[::-1]
l2=len(str5)
for p in range(l2):
    s3=s3+(int(str5[p])*(2**p))
print("decimal sum",s3)
print ("sum of two decimal numbers",s1+s2)
print ("Binary sum: ", r)

binary=input("enter binary number ")
d= int(binary, 2)
print(d)'''

''''import random

print(random.randint(2,122))'''
'''c=0
binary=input("enter any binary number ")
for i in range(len(binary)):
    if binary[i]=='1':
        c+=1
print (f"number of 1's in the binary number {binary} is {c}"  )'''


'''for i in range (1,101):
    if i % 15 == 0:
        print('fizzbuzz', end=' ')
    elif i % 3 == 0:
        print('fizz', end=' ')
    elif i % 5 == 0:
        print('buzz', end=' ')
    else:
        print (i, end=' ')
'''

#label = tk.Label(text="Python rocks!")
#label.pack()

#window.mainloop()


x=1
num=int(input("enter number "))
for i in range(num):
    for j in range(i):
        print (x, end=" ")
        x=x+1
    print(" ")










