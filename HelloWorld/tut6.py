#print ("hello world")
#print ("abhi is learning python","willslowly learn", end=',')
'''my_list1=[4,6,7,8,1,8,18]
my_list2=my_list1.copy()
print(my_list1)
print (id(my_list1))
my_list2.append(70)
print(my_list2)
print(id(my_list2))'''

'''my_dict={"programming":"the process of writing computer programs","abandon": "cease to support or look after",
        "scrabble": "scratch or grope around with one's fingers to find, collect, or hold on to something","desolate":"devoid of inhabitants and visitors"}
name_key=input("Enter the word: ")
if name_key=="programming":
    print(my_dict["programming"])
elif name_key=="abandon":
    print(my_dict["abandon"])
elif name_key=="scrabble":
    print(my_dict["scrabble"])
else:
    print(my_dict["desolate"])'''

'''my_set={'abc':111}
my_list=[1,'abc',55,76,99]
my_tup=(45,88,'abc')
my_dist={}

print(type(my_set))
print(my_list)
print(type(my_dist))
print(my_tup)'''

'''my_dict1={'abhi':'films','rohan':'study','harsh':'sports','papa':True, 12:65, 15:'sitar',4:'alpha'}
my_list=list(my_dict1)
#print(my_dict1.get(13,'not found'))

#for keys, values in my_dict1.items():
    #print(keys,values)

print(my_list)
for items in my_list:
    if str(items).isnumeric() and items>6:
        print(items)'''

'''while (True):
    my_num=input("Enter any number ")
    if int(my_num)<100:
        print("number smaller than 100, try again")
        continue
    else:
        print("yes number greater than 100")
        break
'''
'''list1=[1,2,77,36,44,81]
print(list1[-2:-5:-1])
print(list1[4:-4:-1])'''
#Print Decimal number to Binary number
my_num1=input("Enter any decimal number: ")
my_num=int(my_num1)
final_bin_num=''
while my_num>0:
    bin_num=my_num%2
    final_bin_num=final_bin_num + str(bin_num)
    my_num=my_num//2

final_bin_num=final_bin_num[::-1]
print("The binary number of ",my_num1,"is",final_bin_num)

num_right=int(my_num1)>>3
print(num_right)
print(bin(num_right))








