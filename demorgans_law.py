#Logic operations
A = {"a": 0.4, "b": 0.5, "c": 0.2, "d": 0.6, "e": 0.9}
B = {"a": 0.7, "b": 0.8, "c": 0.9, "d": 0.1, "e": 0}
Anot = {}
Bnot = {}
AunionB = {}
AintersectionB = {}
print("Set A: ", A)
print("Set B: ", B)

AnotintBnot={}
AnotuniBnot={}
for i in A:
    AunionB[i] = max(A[i], B[i])
    AintersectionB[i] = min(A[i], B[i])
    AnotintBnot[i]=min(Anot[i], Bnot[i])
    AnotuniBnot[i]=max(Anot[i], Bnot[i])
print("A union B: ", AunionB)
print("A intersection B", AintersectionB)

#Checking Demorgan
AunionBcomp={}
AintBcomp={}
for i in A: 
  AunionBcomp[i]=round(1-AunionB[i])
  AintBcomp[i]=round(1-AintersectionB[i])

if AunionBcomp==AnotintBnot and AintBcomp==AnotuniBnot:
  print("Demorgan is True")
else: print("Demorgan is False")
