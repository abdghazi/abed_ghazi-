#hackerRank creating list in pyhton question.
#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer e at position i.
#print: Print the list.
#remove e: Delete the first occurrence of integer e.
#append e: Insert integer e at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#we create two litsts we append our input to the first list, then we convert all elements except the commands to intiger values in the list
#then a simple for and if to manipulate the list.



x = int(input())
inputs = []
lists = []
for _ in range(x):
	inputs.append(input().split())
print(inputs)
print(inputs[1])
for j in range(len(inputs)):
	if(len(inputs[j])==3):
		inputs[j][1] = int(inputs[j][1])
		inputs[j][2] = int(inputs[j][2])
	if(len(inputs[j])==2):
		inputs[j][1] = int(inputs[j][1])

print(inputs)


for j in range(len(inputs)):
	if(inputs[j][0]=="insert"):
		lists.insert(inputs[j][1],inputs[j][2])
	if(inputs[j][0]=="print"):
		print(lists)
	if(inputs[j][0]=="remove"):
		lists.remove(inputs[j][1])
	if(inputs[j][0]=="append"):
		lists.append(inputs[j][1])
	if(inputs[j][0]=="sort"):
		lists.sort()
	if(inputs[j][0]=="pop"):
		lists.pop()
	if(inputs[j][0]=="reverse"):
		lists.reverse()
