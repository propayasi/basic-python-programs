"""from this import d


f1=open('t.txt','r')
c=0
d=0
s=f1.read().splitlines()
for i in s:
    if i[0].upper()=='W':
       d+=1
    for j in (i):
        if j.upper()=='W':
            c+=1
print(c,d)"""
"""stk=[]
Top=None
def push(stk,n):
    global Top
    stk.append(n)
    Top=len(stk)-1

def pop(stk):
    global Top
    if len(stk)==0:
        return 'Underflow'
    else:
        p=stk.pop()
        if len(stk)==0:
            Top=None
            return p
        else:
            Top=len(stk)-1
            return p
def display(stk):
    global Top
    for i in range(Top,-1,-1):
        print(stk[i])
while True:
    action=int(input('press 1 to push 2 to pop 3 to display 4 quit '))
    if action==1:
        ask=int(input('pincode of city'))
        ask2=input('name of the city')
        node=[ask,ask2]
        push(stk,node)
    elif action==2:
        c=pop(stk)
        if c=='Underflow':
            print('no value in stk underflow')
            
        else:
            print('popped out node is ',c)
    elif action==3:
        display(stk)
    elif action==4:
        break"""
a=None
a=a+1
print(a)