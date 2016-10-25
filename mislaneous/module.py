# modules are .py files
import datetime

dir(datetime)  # this gives all mehtods present in that file


string = 'a b a a c c a.'
inFile = open('test.txt','r')
line = inFile.read()
print(line)
letters = []

for word in line.split(" "):
    for l in range(0, len(word)):
        if(not word[l]== '\n'):
            letters.append(word[l])



dict = {}
for s in letters:
    if (s in dict)==False:
        if(s not in dict):
            dict[s] =1
    else:
        dict[s] +=1

print(dict)


