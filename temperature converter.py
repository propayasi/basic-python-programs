def CtoF(c):
    f = (9/5)*c+32
    print('Temperature in Fahrenheit:',f)
    
def FtoC(f):
    c = (f-32)*(5/9)
    print('Temperature in Celsius:',c)
    
print('''1. Celsius to Fahrenheit
2. Fahrenheit to Celsius''')

x = int(input('Enter choice:'))
if x == 1:
    t = float(input('Enter temperature in Celsius:'))
    CtoF(t)
elif x == 2:
    t = float(input('Enter temperature in Fahrenheit:'))
    FtoC(t)
else:
    print('Invalid choice')
