import sys

list1 = []
list2 = []

def readFile1():
    with open(sys.argv[1], "r") as file1:
        # Read file1
        for line in file1:
            list1.append(line.split())

def readFile2():
    with open(sys.argv[2], "r") as file2:
        # Read file2
        for line in file2:
            list2.append(line.split())


readFile1()
readFile2()

print()
print("List1 is:", list1[0])
print()
print("list1Length: ", len(list1[0]))
print()
print("List2 is:", list2[0])
print("list2Length: ", len(list2[0]))
print()


listA = list1[0][::-1]
listB = list2[0][::-1]
listC = []

if len(listA) > len(listB):
    a = len(listB)
    b = len(listA) - len(listB)
if len(listB) > len(listA):
    a = len(listA)
    b = len(listB) - len(listA)
for i in range(a):
    for x in range(1):
        listC.append(listA[i])
        listC.append(listB[i])

for c in range(a,a+b):
    if len(listA) > len(listB):
        listC.append(listA[c])
    if len(listB) > len(listA):
        listC.append(listB[c])

with open("output.txt", "w") as outfile:
    for line in listC:
        outfile.write(line + " ")

