# file = open(filepath,mode)

file = open("example.txt",'r')
contents = file.readlines()
# enlève les sauts de ligne
contents = [i.rstrip("\n") for i in contents]

for element in contents:
    print(element)

file.close()
