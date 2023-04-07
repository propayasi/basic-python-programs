"""t1=(10,20,30)
t2=(213,123,213)
t3=t1+t2
print(t3)
print(t2*5 )"""
##################################
"""tp1 = (11,12,15,20,8,9,10)
seq1 = tp1[::2]
seq1 = tp1[5::2]
print(seq1)"""
######################3
##############Unpacking and packing##################### 
"""t1=(10,20,30,40)
print(t1))
print(max(t1))
t2=list(t1)
t2[2]=50
t1=tuple(t2)
print(t1)
print(max(t1))"""
#####################
"""t1=(1,2,3,4,5)
a,b,c,d,e =(p, q, r, s, t)=t1
print(p,q,r,s,t)"""
###########################
####### Write a program that interactively create a nested tuple to store the marks in three subjects for five student .
""""total = ()
for i in range(5):
    mark = ()
    mark1 = int(input("enter the marks of first subject = "))
    mark2 = int(input("enter the marks of second subject = "))
    mark3 = int(input("enter the marks of third subject = "))
    mark = (mark1 , mark2 , mark3)
    total= total + (mark,)
print("total marks = ",total)"""
#################################
"""def find( name):
    if name in tup :
        return name, "is present in ",tup
    else :
        return name, "is not present in ",tup
    
tup = eval( input ("Enter a tuple containing name of student :-"))
nam = input("Enter the name of student :-")

print( find( nam ) )
"""
###################
# #PALINDROME
"""

my_str = input("enter a string")
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")"""
"""
strg=input("enter a string")
count=0
vowels=['a','e','i','o','u']
for i in strg.lower():
    if i in vowels:
        count+=1
    else:
        continue
print("there are about ",count,"in the given string")"""

"""x="Computer Science with python"
print(x[:2], x[:-2],x[-2:], sep="\n")
print(x[6],x[2:4], sep="\n")
print(x[2:-3], x[-4:-2], sep="\n")
"""
"""

p= input("Input your password")
b=len(p)
a=[1,2,3,4,5,6,7,8,9,0]
x=True
if b<7:
     x=False
    
elif int(p[0]) not in a:
        x=False
        
if x==True:
        print("password valid")
else:
    print("invalide")"""
######################################################
#NOTE FUNCTIONS
#FIBONACI
"""
def fibonacci(n):
 if n<=1:
    return n
 else:
    return(fibonacci(n-1))+fibonacci(n-2) # Recursive call

numt=int(input('how many digits do u want)'))
for i in range(numt):
    print(fibonacci(i))"""
####################
#FACTORIAL
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter a number"))
print(factorial(num))"""
####################### change the odd positions to even 
"""a=eval(input("enter"))
print(a)
b=len(a)
if b%2 !=0:
    c=int(input('enter another value pls '))
    a.append(c)    
for i in range(0,b,2):
    a[i],a[i+1]=a[i+1],a[i] #a,b=b,a that logic
print(a)"""
#######################

