# Define a matrix A
A = []
print("Enter 9 Elements for First Matrix: ")
for i in range(3):
    A.append([])
    for j in range(3):
        num = int(input())
        A[i].append(num)

# Define an empty matrix of reverse order  
transResult = [[0, 0, 0],    
                             [0, 0, 0],  
                             [0, 0, 0]]  
# Use nested for loop on matrix A  
for a in range(len(A)):    
   for b in range(len(A[0])):    
          transResult[b][a] = A[a][b] # store transpose result on empty matrix          
# Printing result in the output  
print("The transpose of matrix A is: ")  
for res in transResult:    
   print(res)  
