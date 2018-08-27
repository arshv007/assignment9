#Ques1
#Ans. ZeroDivisionError
a=3
try:
  if a<4:
    a=a/(a-3)
    print(a)

except ZeroDivisionError:
  print("zero division error")


#Ques2

#Ans. Error occured is IndexError(i.e. index out of range) for which we use try-except block 
try:
  l=[1,2,3]
  print(l[3])

except IndexError:
  print("index error")

#Q3. What will be the output of the following code:

# Program to depict Raising Exception
'''
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or n
    '''
'''
#Output
An exception
Traceback (most recent call last):
  File "hello.py", line 2, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there
'''

#Ques4

# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print( "a/b result in 0")
	else:
		print( c)
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
'''
#Output:-
-5.0
a/b result in 0
'''

#Ques5
#1. Import Error
try:
  from abc import a
  print(a)
except ImportError:
  print(" Import Error:")

#2. Value Error
try:
  num=int(input("Enter number: "))
  print(num)
except ValueError:
  print("Value Error")

#3. Index Error
l=[5,1,2,4]
try:
  print(l[5])
except IndexError:
  print(" Index Error")
