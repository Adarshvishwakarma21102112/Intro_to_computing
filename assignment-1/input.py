#assignment 1

#Ques1
print('ans 1\n')

numb1=float(input("enter first number: "))
numb2=float(input("enter second number: "))
numb3=float(input("enter third number: "))
sum=numb1+numb2+numb3
avg=sum/3
print(avg)



#Ques2
print('______________________________________________________________________')
print('\nans 2\n')

r=0.20                                             #r= Tax Rate
sd=10000                                           #sd= Standard Deductions
dd=3000                                            #dd= Dependent Deduction
gross=float(input("enter gross income: "))
nd=float(input("enter no. of dependents: "))       #nd= No. of Dependents
ti=gross-sd-(dd*nd)                                #ti= Taxable Income
tax=ti*r
print(tax)



#QUES3.
print('________________________________________________________________________')
print('\nans 3\n')

print('Student[SID, Name, Gender, Course name, CGPA]')
Student=[21102112, 'Adarsh Vishwakarma', 'M', 'Civil', 8.5]
print('Student=', Student)



#Ques4
print('______________________________________________________________________')
print('\nans 4\n')

print('Marks of five students')
Marks=[100, 55, 85, 67, 77]
print('List before sorting', Marks)
Marks.sort()
print('List after sorting', Marks)



#Ques5
print('_______________________________________________________________________')
print('\nans5\n')
print('\n(a)\n')
#(a)

Colour=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Colour.pop(3)
print('Colour',Colour)

print('\n(b)\n')
#(b)

Colour=['Red','Green','White', 'Black', 'Pink', 'Yellow']
Colour[3:5]=['Purple']
print('Colour',Colour)
