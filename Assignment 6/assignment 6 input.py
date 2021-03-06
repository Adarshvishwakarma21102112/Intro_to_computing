                                #Assignment 6
print("Ans 1")

def perfect_number(n):                    #define a function for checking the number is perfect or not

    sum = 0                             
    for x in range(1, n):               #for perfect no. sum of all divisors are equal to that no.
        if n % x == 0:                  
            sum += x
    return sum == n
n=int(input("enter the number :"))
if perfect_number(n)== True:
    print(n,",this is perfect number")
else:
    print(n,",this is not a perfect number")

#_________________________________________________________________________________________________________________________
print("\nAns 2")
                                            #define function for checking word or phrase are Palidrome or not
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1               # for Palindrome left position of word from forward
    while right_pos >= left_pos:               #for Palindrome right position of word from backward
        if not string[left_pos] == string[right_pos]:     #left position word and right position should be same
            return False
        left_pos += 1
        right_pos -= 1
    return True
str = input("enter the word :")
print(isPalindrome(str))

#__________________________________________________________________________________________________________________________
print("\nAns 3")                       #python program for making Pascal Triangle
                                                           
def pascal_triangle(n):                            
   trow = [1]
   y = [0]
   for x in range(1,n+1):
      print(" "*(n-x),trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
n=int(input("enter the no of rows :"))
pascal_triangle(n) 

#____________________________________________________________________________________________________________________________
print("\nAns 4")                      #python program for checking string is pangram or not 
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"           #pangram is all character of alphabet is available 
    for char in alphabet:
        if char not in str.lower():           # if all the characters are available then return True
            return False                        #otherwise False
  
    return True
string = input("enter the string :")
if(ispangram(string)==True):
    print("yes, ",string, ", this string is Pangram")
else:
    print("No, ",string,", this string is not Pangram")

#______________________________________________________________________________________________________________________________
print("\nAns 5")
items=[n for n in input("enter the words: ").split()]       
items.sort()                                             #short function work to arrange the letters in alphabatically order
print("alphabetically arranged words:")
print('-'.join(items))
#______________________________________________________________________________________________________________________________
print("\nAns 6")
def student_data(student_id, **kwargs):                     #define function and parameter as kwargs
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name:  {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class:  {kwargs['student_class']}")

 
student_data(student_id='21102112', student_name='Adrsh vishwakarma')

student_data(student_id='21102110', student_name='Adarsh vishwakarma', student_class ='Btech 1st year')
#________________________________________________________________________________________________________________________________
print("\nAns 7")
class Student:                              #define class function for printing student marks and student name
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 

#________________________________________________________________________________________________________________________________
print("\nAns 8")

class solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


#________________________________________________________________________________________________________________________________
print("\nAns 9")

class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))

