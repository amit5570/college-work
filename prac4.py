#prac 5
import numpy as np      
b=np.array([[1,2,1],[2,1,0],[3,0,2]])
print("The matrix M is:",b)
a=np.linalg.det(b)
if a==0:
    print("Matrix is not invertible is")
else:
    binv=np.linalg.inv(b)
    print("The inverse of matrix M is",binv)
    


