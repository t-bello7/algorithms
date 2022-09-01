#variables

#list #list methods
#tuples #tuples methods
#dictionaries #dictionaries methods

#conditional statement ...#and #or

#loop while , for , 
import oop

x = 5

if x < 2 : #false
    print ('small')
elif x < 10: #medium
    print ('Medium')
else:
    print('Large')


#a dysfunctional

if x < 2 :
    print ('Below 2')
elif x >= 2:
    print ('Two or More')
else : #this would never be printed regardless if the number 
    print ('Something else')

#You surround a dangerous section of code with try and except

#If the code in the try works - the except is skipped
#If the code in the try fails - It jumps to the except section
#e.g  
# astr = 'Hello Bob'
# istr = int(astr)
# print('First', 'istr')
# astr ='123'
# istr = int(astr)
# print('Second', istr)
# this codes give the error
# Traceback (most recent call last):
#   File "c:\Users\Obij2\Desktop\tomi borrowing space\learningpython.py", line 37, in <module>
#     istr = int(astr)
# ValueError: invalid literal for int() with base 10: 'Hello Bob'

# Using the try and error we have: ..also refer to the sampletryexcpet in the folder
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '1234'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)


## string mehtods

# You can slice strings like lists
# you can check the len of strings with a function call
# yon use .strip() method for the string 
# you can use find() method to search for the postion of a letter in a string