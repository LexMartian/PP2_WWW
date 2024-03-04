chars = ['a', 'b', 'c', 'd']
with open('list.txt', "w") as myfile:
        for c in chars:
                myfile.write("%s\n" % c) #%s это каждый 'c' + новая строка

content = open('list.txt')
print(content.read())
