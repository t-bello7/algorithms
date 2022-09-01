#amazing we are going to read a file and find the most 10 common words
# by using the tuples, dictionaries and list
#as we know the file is a list of stirngs
# and string itself is a list

open_file = open('romea.txt')
counts = dict()
for line in open_file:
    words = line.split()
    words is a list of words
    # split will split the words in a line cos of the whitespace
    for word in words():
        count[word] = counts.get(word, 0) +1 #this line is an idiom for making histogram
        #the get method of the dictionaries is used to avoid KeyError.Returns the value of a given key if present
        #Dict.get(key, default=None) second parameter prints the error messge you want

list_file = list()
for key, val in counts.items():
    #.itmes convets a dictionary to a list of tuples (key, value)
    newtup = (val,key)
    list_file.append(newtup)

list_file = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print (key, val)
#learn lambda nd regex
# or 

print(sorted([(v,k) for v,k in  c.items()]))