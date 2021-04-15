dictionaryOne ={}

aSampleList = [1,2,3,4]


#add values to dictionaryOne
#Method 1
dictionaryOne = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key7' :[ 'value2', 'value4']
}

#or method 2

dictionaryTwo = {}

dictionaryTwo['key4'] = 'value4'
dictionaryTwo['key5'] = 'value5'
dictionaryTwo['key6'] =  'value6'


print(aSampleList)  
print(dictionaryOne)
print(dictionaryTwo)

#to delete a value
dictionaryOne.pop('key1')

#for looping a dictionary
# for each key value pair in items in dictionaries 
for key,value in dictionaryTwo.items():
    print("I have"+key+" relating with " +value)
    print("list in dictionarisies" + key7[1])

print(dictionaryOne)