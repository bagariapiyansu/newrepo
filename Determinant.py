def printM(x,l):
    for i in range(l):
        print(' '.join(map(str, x[i])))
    print()
def det(L):
    M=L[0];n=L[-1]
    A_int=[[int(M[i][j]) for j in range(n)] for i in range(n)]
    M_r1=[]
    for j in range(n):
     temp=[[A_int[i][j] for j in range(n)] for i in range(n)]
     #printM(temp,n)
     if n>=3:
      del temp[0]
      for i in range(n-1):
         del temp[i][j]

     M_r1.append(temp[0][0]*temp[1][1]-temp[0][1]*temp[1][0])
     #print(M_r1)
     #printM(temp,n-1)
     #printM(A_int,n)
    if n==3:
      C_r1=[]
      for i in range(n):
         C_r1.append(((-1)**(-i))*M_r1[i])
      #print(C_r1)
      d=0
      for i in range(n):
         d+=C_r1[i]*A_int[0][i]
      return(d)
    else:
       d=M_r1[0]
       return(d)

def inputmat():
   n=int(input("Enter the size of matrix: "))
   print("Enter an {}X{} matrix\n".format(n,n))
   A_s=[]
   for i in range(n):
       A_s.append((input()).split())
   #print("\nThe entered matrix is:\n")
   #for x in A_s:
   #    print(' '.join(x))
   return([A_s,n])


print(det(inputmat()))





