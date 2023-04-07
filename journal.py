
#NOTE  IF USING THE CODE REMOVE THE RESPECTIVE TRIPLE COMMAS OR THE CODE WONT WORK
# BASIC FUNCTIONS OF LISTS TUPLES AND DICT 
#1) #################
'''list1=eval(input("Enter"))
odd=[]
even=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd,"odd")
print(even,"even")'''
#2)##############
"""list1=eval(input("enter a list"))
print(max(list1))
print(min(list1))
a=0
countodd=0
counteven=0
for i in list1:
    a+=i
    if i%2==0:
        counteven+=1
    else:
        countodd+=1
print(countodd,"odd",counteven,"even")
print(a)"""
########################################
"""list1=eval(input("enter a list"))
list2=[]
for i in list1:
    if i%2==0:
        i=i+2
        list2.append(i)
    else:
        i=i+1
        list2.append(i)
print(list2)"""
#4#####################################3
"""tup1=eval(input("enter a tuple"))
tup2=[]
for i in tup1:
    if i not in tup2:
        tup2.append(i)
    else:
        print("dupped values",i)
print(tuple(tup2))"""
#5)######################################333
"""num1=int(input("n number"))
d={}
for i in range(num1):
    num2=eval(input("roll name"))
    num3=input("name")
    d[num2]=num3
enter1=int(input("Roll number of kid"))
print(d[enter1])"""
#6)#######################################33
"""num1=int(input("n number"))
d1={}
for i in range(num1):
    num2=eval(input("roll name"))
    num3=eval(input("marks"))
    d1[num2]=num3
print(d1,"original dict")
d2={}
for i in d1:
    d2[i]=sum(d1[i])
print(d2,"summed up dict")"""

#7###################################
"""d1={}
num1=int(input("enter"))
for i in range(num1):
    employeid=int(input("enter key"))
    d1[employeid]={}
    employe1=input("name")
    employe2=int(input("age"))
    employe3=int(input('salary'))
    d1[employeid]['name']=employe1
    d1[employeid]['age']=employe2
    d1[employeid]['salary']=employe3
print(d1.keys())
ask1=int(input("Id of the candidate"))
if ask1 in d1:
  ask=int(input('1)all possibilites 2)salary 3)age 4)name'))
  if ask==1:
      print(d1)
  elif ask==2:
          print(d1[ask1]['salary'])
  elif ask==3:
         print(d1[ask1]['age'])
  elif ask==4:
         print(d1[ask1]['name'])
else:
                print('candidate doesnt exist')"""
#9)####################################
"""
d1={}
d2={}
num1=int(input("enter"))
for i in range(num1):
    id_=int(input("student id"))
    vals=int(input("phone number"))
    d1[id_]=vals
a=list(d1.values())
b=list(d1.keys())
d2=dict(zip(a,b))
print(d2)    """
#10)####################################
"""lst=eval(input('lists'))
lst2=[]
for i in range(len(lst)):
    lst2.append(i)
    lst2[i]=lst[i][1:]
print(lst2)"""
"""
num1=int(input('enter num'))
a=[]
for i in range(num1):
    b=int(input("value"))
    a.append(b)
print(a)
print(a[-1::]+a[:-1])"""
###########10 variety if not using eval
"""num=int(input("how mant values u want"))
a=[]
for i in range(num):
    b=input('value')
    a.append(b)
for j in range(len(a)):
    a[j]=a[j][1::]
print(a)"""
