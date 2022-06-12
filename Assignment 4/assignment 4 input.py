                              #Assignment 4
#________________________________________________________________________________________________________________________________

print("Ans 1")
n=int(input("enter the marks:"))
if n<25 :                                  #grade for below 25
    print("correspinding grade","=","F")
elif n>=25 and n<45 :                       #grade for 25 to 45
   print("correspinding grade","=","E")
elif n>=45 and n<50 :                       #grade for 45 to 50
    print("correspinding grade","=","D")
elif n>=50 and n<60 :                       #grade for 50 to 60
    print("correspinding grade","=","C")
elif n>=60 and n<80 :                       #grade for 60 to 80
    print("correspinding grade","=","B")
elif n>=80 and n<=100 :                     #grade for above 80 and max to 100
    print("correspinding grade","=","A")
else :                                       # grade for above 100 which is not defined
    print("not defined")


#____________________________________________________________________________________________________________________

print("\nAns 2")
                           #program to find year is leap year or not
year = int(input("enter year:"))
if year % 400 == 0 :         #if year is divisible by 400 then it is leap year
    print(year, "is a Leap Year")
elif year % 100 == 0 :        # year is divisible by only 100 then it is not leap year
    print(year, "is not a Leap Year")
elif year % 4 == 0 :          # year is divisible by 4 when it is not divisible by 100 
    print(year, "is a Leap Year")
else :
    print(year, "is not a Leap Year")

#_____________________________________________________________________________________________________________________________

print("\nAns 3")
                                #python program for multiplication game
                            #import random
import random            
                                       #no of problems want
gamenumber = int(input("How many probems do you want?\n"))  

count = 1
while count <= gamenumber:
    num_1 = random.randint(0,9)       #taking randomly any no between 0 and 9 inclusively
    num_2 = random.randint(0,9)
    print("\nQuestion",count,":",num_1,"X",num_2)
    guess = int(input())
    answer =(num_1*num_2)
                                     # when input answer is correct
    if guess == answer:       
        
        print("Right!")
    else:                             #when input anser is wrong
        print("Wrong, the answer is", answer, ".")
    count=count+1

        
#____________________________________________________________________________________________________________________________________

print("\nAns 4")
x=200                          #we know candies are less than 200
for candies in range (x):                     #we use range function using for 
    if candies%5==2:                 # if candies are divide by 5 reminder should be 2
        if candies%6==3:             # if candies are divide by 6 reminder should be 3
            if candies%7==2:         # if candies are divide by 7 reminder should be 2
                print("no of candies present in the bowl","=",candies)
                break
                

    
