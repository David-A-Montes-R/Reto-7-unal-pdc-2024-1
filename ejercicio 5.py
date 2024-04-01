#imprimir el factorial de un número n dado

def factorial_casero(n:int):
    m=n
    if n==0:
        return 1
    elif (n>0):
        while(n>1):
            n=n-1
            m=m*n
    return m

if __name__=="__main__":
  n=int(input("introduzca un numero n, para conocer su factorial n!:"))
  f=factorial_casero(n)
  if n>=0:
    print("el factorial del número",n,"es:",f)
  else:
     print("no es posible calcular el factorial de un número negativo")
      
