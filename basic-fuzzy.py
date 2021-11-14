#Logic operations
A = {"a": 0.4, "b": 0.5, "c": 0.2, "d": 0.6, "e": 0.9}
B = {"a": 0.7, "b": 0.8, "c": 0.9, "d": 0.1, "e": 0}
Anot = {}
Bnot = {}
AunionB = {}
AintersectionB = {}
print("Set A: ", A)
print("Set B: ", B)
for i in A:
    Anot[i] = round(1 - (A[i]))
    Bnot[i] = round(1 - B[i])
print("A Complement: ", Anot)
print("B Complement: ", Bnot)
for i in A:
    AunionB[i] = max(A[i], B[i])
    AintersectionB[i] = min(A[i], B[i])
print("A union B: ", AunionB)
print("A intersection B", AintersectionB)

