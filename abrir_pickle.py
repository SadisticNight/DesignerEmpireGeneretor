import pickle as A
with open('celdas.pkl','rb')as B:C=A.load(B)
for D in C['celdas'][:1]:print(D)
