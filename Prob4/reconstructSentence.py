# reconstructSentence.py takes 2 arguments file1 and file2
# Example: python3 reconstructSentence.py input1.txt input2.txt

import sys

# Variable for list
list1 = []
list2 = []

# Function to read file1
def readFile1():
    with open(sys.argv[1], "r") as file1:
        # Read file1
        for line in file1:
            list1.append(line.split())
# Function to read file2
def readFile2():
    with open(sys.argv[2], "r") as file2:
        # Read file2
        for line in file2:
            list2.append(line.split())
# Call out functions
readFile1()
readFile2()
# Rearrange lists from file1 and file1
listA = list1[0][::-1]
listB = list2[0][::-1]
# Append final result
listC = []
# Check to see if listA > listB?
if len(listA) > len(listB):
    a = len(listB)
    b = len(listA) - len(listB)
# Check to see if listB > listA?
if len(listB) > len(listA):
    a = len(listA)
    b = len(listB) - len(listA)
# For every elements in the list
for i in range(a):
    for x in range(1):
        # Combines their contents
        listC.append(listA[i])
        listC.append(listB[i])
# Check the contents
for c in range(a,a+b):
    if len(listA) > len(listB):
        listC.append(listA[c])
    if len(listB) > len(listA):
        listC.append(listB[c])
# Print out the output
print()
print("List1 is:", list1[0])
print()
print("list1Length: ", len(list1[0]))
print()
print("List2 is:", list2[0])
print("list2Length: ", len(list2[0]))
print()
print("The list out is: ", listC)

# Write out the output into the different file
with open("output.txt", "w") as outfile:
    for line in listC:
        outfile.write(line + " ")

