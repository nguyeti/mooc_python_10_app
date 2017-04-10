# file = open(filepath,mode)
# a mode = append mode, n'écrase pas le contenu actuel
# file = open("blabla.txt",'r')
# file2 = open("example.txt",'a+')

# contents = file.readlines()
# #contents = [i.rstrip() for i in contents]
#
# for content in contents:
#     file2.write(content)
#     print("Writing " + content)
#
# file2.seek(0)
# contents2 = file2.readlines()
# contents2 = [i.rstrip() for i in contents2]
#
# for content in contents2:
#     print(content)
#
# file.close()
# file2.close()


# with statement > don't need to close the file at the end
with open("blabla.txt",'r') as file:
    with open("example.txt",'a+') as file2:
        file.seek(0)
        contents = file.readlines()
        for content in contents:
            file2.write(content)
            print("Writing " + content)
        file2.seek(0)
        contents2 = file2.readlines()
        for content in contents2:
            print(content)
