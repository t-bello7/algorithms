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