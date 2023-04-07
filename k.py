#1 
"""def cel_to_far(a):
    F=1.8*a+32
    print('fahrenheit reading is',F)

def far_to_cel(a):
    C=(a-32)*5/9
    print('celsius reading is',C)

ask=int(input('''choose 1 for celsius to fahrenheit
2) for fahrenheit to celsius'''))

if ask ==1:
    cel=float(input('celsius reading'))
    cel_to_far(cel)

elif ask ==2:
    far=float(input('fahrenheit reading'))
    far_to_cel(far)

else:
    print('invalid')
"""

#2)
"""def area(r):
    print('area =',3.14*r*r)

def circ(r):
    print('circumference =',2*3.14*r)

ask=int(input('1) area 2)circumference'))
ask2=float(input('radii'))

if ask==1:
    area(ask2)

elif ask==2:
    circ(ask2)

else:
    print('invalid')"""

#3)
"""c=0
with open('t.txt','r') as f:
    k=f.readlines()
    print('no. of line are',len(k))
    for i in k:
        if i[0]=='A':
            c+=1
    print(c)       """


#4)
"""c=0
with open('t.txt') as f:
    k=f.read().split()
    print('total no. of words are',len(k))
    for i in k:
        if i[0]=='S':
            c+=1
    print('no of words with S are ',c)"""

#5)
"""f=open('t.txt')
k=f.read()
p=['a','e','i','o','u']
v=0
c=0
l=0
for i in k:
    if i.lower() in p:
        v+=1
    if i.isupper()==True:
        c+=1
    elif i.islower()==True:
        l+=1
print(f'''no. of vowels are {v} 
no. of capitals are {c}
no of lowercase are {l}''')
f.close()
"""
#6)
"""f=open('t.txt')
c=[]
k=f.read().split()
for i in k:
    if len(i)>5:

        c.append(i)
    else:
        continue
f.close()
f1=open('tt.txt','w')
for i in c:
    f1.write(i)
    f1.write('\n')
f.close()
"""
#7)
"""f=open('t.txt')
k=f.read().split()
for i in k:
    i=i[::-1]
    print(i)
f.close()"""
