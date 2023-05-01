l1=[]
dic={}
nn=eval(input())              # Takes input for number of groups
for i in range(nn):
    su=list(set(list(map(int,input().strip().split()))))   # Takes input for each group and appends the elements to a list l1
    l1.append(su)

a,b=input().strip().split()   # Takes input for starting and ending elements

universal=[]
for i in l1:
    universal+=i              # Creates a list universal containing all the elements in all the groups
n=max(set(universal))+1      # Finds the highest element in universal and adds 1 to it
var=0
graph=[[[0,0] for i in range(n)] for j in range(n)]  # Initializes a 3D list graph with zeros and size nxn

# Loops through the elements in the graph and creates edges between elements in the same group
# Stores the group id for each edge in the second dimension of the graph
for i in range(n):
    for j in l1:
        var+=1
        if i in j:
            for k in j:
                if i!=k:
                    graph[i][k][0]=1
                    graph[i][k][1]=var #for group id
    var=0

lookup=[0 for i in range(n)]      # Initializes a list lookup with zeros and size n to keep track of visited elements
lookup[int(a)]=1                  # Marks the starting element as visited
lookup_group=[0 for i in range(nn+1)]  # Initializes a list lookup_group with zeros and size nn+1 to keep track of visited groups
l2=[[99999999,999999999]]        # Initializes a list l2 with a nested list containing two large integers

def backtrack(x,s,cost):
    # The backtrack function recursively searches for a path from a to b using a depth-first search algorithm
    if x==int(b):        # If we reach the ending element, update l2 with the path and its cost
        if cost<l2[0][0]:
            l2[0][0]=cost
            l2[0][1]=s  
        return
    for i in range(n):
        if lookup[i]==0 and graph[x][i][0]==1 and lookup_group[graph[x][i][1]]!=2:
            # If the element is not visited, it has a direct edge to the current element, and the group of the edge is not already visited
            # Mark the element and the group as visited, and recursively call the backtrack function with the new element and updated path and cost
            lookup[i]=1
            lookup_group[graph[x][i][1]]+=1
            backtrack(i,s+str(i)+" ",cost+1)
            lookup_group[graph[x][i][1]]-=1
            lookup[i]=0

backtrack(int(a),"",0)   # Calls the backtrack function with starting element, empty path and zero cost
if l2[0][1]==999999999:
    print("None")
else:
    print(a+" "+str(l2[0][1][:-1]))   # Prints the path found
