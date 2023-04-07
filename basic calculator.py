def add():
        x= float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print( x + y)
 
def subtract():
        x= float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print( x - y)
 
def multiply():
        x= float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print( x *y)

 def divide():
        x= float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print( x / y)

ans=‘y’
while ans==‘y’ or ans==‘Y’:
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int(input(‘Enter option number’))
        if choice == 1:
             add()
        elif choice == 2:
             subtract()
        elif choice == 3:
             multiply()
        elif choice == 4:
               divide()         
        else:
               print("Invalid Input")
ans=input(‘You want to continue? (y/n)’ )

