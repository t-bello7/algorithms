# Iterative loops
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    elif line == 'done':
        break
    else:
        print('Not a valid Response')
    print(line)
    
print('Done !')

#definit loops run the excat number of times
for i in range(6):
    print(i)

# Making smart loops

list  = [34,45,66,33]
# adding value in a list
for i in list:
    sum = i + []
    print(sum)

#what is the largetst number?
largets_num = -1
for i in list:
     #changing of variable in a for loop
    if largets_num < i :
        largets_num = i 
