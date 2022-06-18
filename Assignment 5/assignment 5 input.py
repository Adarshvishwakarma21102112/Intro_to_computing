                                  #Assignment 5
print("Ans 1")
                                 #python program for reverse the string
def reverse(string):               #define the reverse function
    string = string[::-1]                #using extended slice syntax
    return string
s= str(input("write the string:"))
print("original string:",s)
print("the reversed string:",reverse(s))

#______________________or another method___________________________________________________________________________________
print("or")
print('\nAns1 ')
                           #python program for reverse the string
def reverse(s):              #define the reverse function
    str = " "
    for i in s:               #using loop to reverse the string
        str = i+str
    return str

s= str(input("write the string:"))
print("original string:",s)
print("reversed string is:",reverse(s) )

#_________________________________________________________________________________________________________________________
print("\nAns 2")
                                      #python program to print all values in range divisible by given no.
lower = int(input("Enter the lower range limit:"))        #input the lower limit
upper = int(input("enter the upper range limit:"))        #input the upper limit
n = int(input("enter the number to be divided by:"))      #input the no which is divide
for i in range (lower,upper+1):           #using loop in range
    if (i%n)==0:
        print(i)

#_______________________________________________________________________________________________________________________
print("\nAns 3")
import math                    #for heroin's formula we have to import math
a =int(input("enter the first length of triangle:"))                #1st length of triangle
b =int(input("enter the second length of triangle:"))               #2nd length of triangle
c =int(input("enter the third length of triangle:"))                 #3rd length of triangle
if a+b<c or b+c<a or c+a<b:         #condition for triangle is formed or not
    print("the triangle is not possible by this combination")
else :
    print("the triangle is possible by this combination of sides")
    s=(a+b+c)/2                           #s is defined has half of perimeter of triangle.                       
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))    #Heroin's formula
    print("Area of the triangle:",area)


#_________________________________________________________________________________________________________________________
print("\nAns 4")
                                        #python program to construct pattern using nested loop
n=5                                     #using loop for pattern
for i in range (n):                     # outer loop for ith rows
    for j in range(i):                  #inner loop for jth columns
        print("*",end=" ")
    print('')   
        
for i in range(n,0,-1):                #it for another downward triangle
    for j in range(i):
        print("*",end=" ")
    print(' ')

#__________________________________________________________________________________________________________________________
print("\nAns 5")

n= int(input("enter the no of rows:"))

asciichr = 65

                                 # outer loop for ith rows
for i in range(0,n):
                                # inner loop for jth columns
    for j in range(0,i+1):
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
        if asciichr>=91:
            asciichr = 65
    print()

#___________________________________________________________________________________________________________________________
print("\nAns 6")

lower_value = int(input("enter the lower range :"))      #input the lower limit 
upper_value = int(input("enter the upper range :"))           #input the upper limit
print ("The Prime Numbers in the range are: ")        
for number in range (lower_value, upper_value + 1):        #using for loop
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:                     #for prime no it is not divisible by any other no except self and 1 
                break  
        else:  
            print (number)  
    
#__________________________________________________________________________________________________________________________
print("\nAns 7")
                                         #python program for find no multiple of 7 and divisible by 11
for i in range (1,500):
                                              # range is 1-500
    if i%7==0 and i%11==0:
        print(i)

#__________________________________________________________________________________________________________________________
print("\nAns 8")
arr=[]
for i in range (10): 
    a=int(input("enter the values: "))
    arr.append(a)
print(arr)    
    
print("\nAns 8(a)")                        
print("positive numbers:")
for i in arr:                            #for positive nos the number should be greater than zero
    if i>0:
        print(i,end=" ")
        
print("\nAns 8(b)")
print("negative numbers:")                   
for i in arr:                       #for negative nos the number should be less than zero
    if i<0:
        print(i,end=" ")
        
print("\nAns 8(c)")
print("odd numbers:")                 #for odd nos number should not be divisible by 2
for i in arr:
    if i%2 != 0:
        print(i,end=" ")

print("\nAns 8(d)")
print("even numbers:")
for i in arr :                   #for even nos number should be divisivle by 2
    if i%2 == 0:
        print(i,end=" ")
        
print("\nAns 8(e)")
print("no of times each no occur in list:")

g=[]
for i in arr:          #using for loop
    counts=0                                                           
    if i in g:         
         continue
    else:
        g.append(i)       #making the list of count nos
        for ele in arr:
            if ele==i:
                counts=counts+1 
        print("count of",i, '=',counts)

   
#________________________________________________________________________________________________________________________________
print("\nAns 9")
n=int(input("Number of words: "))
li=[]
for i in range(n):
    word=input("Enter the word: ")
    li.append(word)
times={}
for i in li :
    if i not in times :
        times[i]=1
    else :
        times[i]+=1
print("Number of occurences: ",times)


    
