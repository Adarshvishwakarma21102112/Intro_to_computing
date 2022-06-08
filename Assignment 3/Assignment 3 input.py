print("Ans 1")
                                      #program to convert a number into its binary
decimal=int(input("enter a decimal number:\n"))
binary = 0
ctr = 0
temp=decimal
                                    #find binary value using while loop
while temp>0:
    binary = ((temp%2)*(10**ctr)) + binary
    
    temp=int(temp/2)
    ctr += 1
print("binary of decimal:",binary)
    
#__________________________________________________________________________________________________________________

print("\nAns 2")
                # Python program for simple calculator
 
                # Function to add two numbers
def add(num1, num2):
    return num1 + num2
 
                 # Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
 
                   # Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
                  # Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select=int(input('select operation from 1,2,3,4 :'))
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
                                               #using if elif else function
if select==1 :
    print(num1,'+',num2, '=', add(num1,num2))
elif select==2 :
    print(num1, '-', num2, '=', subtract(num1,num2))
elif select==3 :
    print(num1 ,'*', num2, '=', multiply(num1,num2))
elif select==4 :
    print(num1,'/',num2,'=' ,divide(num1,num2))
else :
    print('invalid input')

#_Ans3___________________________________________________________________________________________________________________

print('\nAns3')

import math
#(a)
print('\n(a)')
                        #python expression is
                  #the parantheses around 5 are redundant
a = (3+4)*5
print('(3+4)*5','=',a)

#(b)

print("\n(b)")
n=int(input('enter value of n:\n' ))
                    #python expression is
b = n*(n-1)/2
print("n*(n-1)/2","=",b)

#(c)
print("\n(c)")
r = int(input("enter value of r:"))
                     #use of math.pi for python expression
c=4*math.pi*r**2
print('4*math.pi*r**2','=',c)

#(d)
print('\n(d)')
r=int(input('enter value of r:'))
a=int(input('enter value of a:'))
b=int(input("enter value of b:"))
      
              #python expression using math module sqrt,cos,sin
d=math.sqrt(r*math.cos(a)**2 + r*math.sin(b)**2)
print("math.sqrt(r*math.cos(a)**2 + r*math.sin(b)**2)","=",d)

#(e)
print("\n(e)")
x1 = int(input("enter value of x1:"))
x2 = int(input("enter value of x2:"))
y1 = int(input("enter value of y1:"))
y2 = int(input("enter value of y2:"))
               #python expression is
if x1!=x2:
    e= (y2-y1)/(x2-x1)
    print("(y2-y1)/(x2-x1)","=",e)
else :
    print("invalid input division by zero not possible")

#Ans4_______________________________________________________________________________________________________________________    
print('\nAns(4)')
#(a)
print('\n(a)')
print('values of i :')         #for showing sequence of no in range use for loop
for i in range(5):
    print(i) 

#(b)
print('\n(b)')
print("values of i:")             #for showing sequence of no in range use for loop
for i in range(3,10):
    print(i)
#(c)
print('\n(c)')           
print("values of i:")             #for showing sequence of no in range use for loop
for i in range(4,13,3):
    print(i)

#(d)
print('\n(d)')           
print("values of i:")           #for showing sequence of no in range use for loop
for i in range(15,5,-2):
    print(i)
#(e)
print('\n(e)')           
print("values of i:")      #for showing sequence of no in range use for loop
for i in range(5,3):
    print(i)               #it has no output 

#Ans5_______________________________________________________________________________________________________________________________

print('\nAns5')
H = int(input("enter no of hydrogen atoms :"))
C = int(input("enter no of carbon atoms:"))
O = int(input("enter no of oxygen atoms:"))
atom_weigh_of_H = 1.00794         #atomic weight of hydrogen
atom_weigh_of_C = 12.0107         #atomic weight of carbon
atom_weigh_of_O = 15.9994         #atomic weight of oxygen
molecular_weigh = (H*atom_weigh_of_H + C*atom_weigh_of_C + O*atom_weigh_of_O)
print('the molecular weight of molecule:',molecular_weigh)
        
