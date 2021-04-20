xfile = open('hello.txt')
count = 0

#python reads line by line of the text file
for chess in xfile:
    count += 1
    print (count,chess)

for chess in xfile:
    chess_striped = chess.rstrip(f)
    if chess.startswith('from'):
        print(chess_striped)

## read 10 million lines is problem
# check methods or open object  
text_file = xfile.read()
print(len(text_file))

