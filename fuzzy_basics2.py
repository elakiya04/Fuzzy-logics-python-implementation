def complelement(A):
  Acomp={}
  for i in A: 
    Acomp[i]=round(1-A[i], 2)
  return Acomp 
def union(A, B): 
  union={}
  for i in A: 
    union[i]=max(A[i], B[i])
  return union
def intersection(A, B): 
  intersection={}
  for i in A: 
    intersection[i]=min(A[i], B[i])
  return intersection



A = {"a": 0.4, "b": 0.5, "c": 0.2, "d": 0.6, "e": 0.9}
B = {"a": 0.7, "b": 0.8, "c": 0.9, "d": 0.1, "e": 0}

print(complelement(B))
print(complelement(A))
print(union(A, B))
print(intersection(A, B))
