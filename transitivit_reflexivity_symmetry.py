import numpy as np
def symmetric(A): 
  (m,n)=np.shape(A)
  x=[]
  for i in range(0, m): 
    for j in range(0, n): 
      if (A[i, j])==(A[j, i]): 
        x.append(True)
      else: x.append(False)
      if all(x)==True: 
        a=True
      else: a=False
  return a
def reflexive(A): 
  (m,n)=np.shape(A)
  y=[]
  for i in range(0, m): 
    for j in range(0, n): 
      if all(A[i])==all(A[j]): 
        y.append(True)
      else:y.append(False)
      if all(y)==True: 
        b=True
      else: b=False
  return b
def transitive(A): 
  if symmetric(A)==True and reflexive(A)==True:
    c=True
  else: c=False
  return c
A = np.array([[1, 0.4, 0.8, 0.2, 0.3],
    [0.6, 1 ,0, 0, 0.8], 
    [0, 0.4, 1, 0.8, 0.4], 
    [0.2, 0, 0, 0.9, 0.5], 
    [0.3, 0.8, 0.9, 0.5, 1]])
print("Symmetry is", symmetric(A))
print("Refelexitivity is",reflexive(A))
print("Thus, Transitivity is",transitive(A))
