# implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores
# apunte importante: todos los números naturales se pueden interpretar como la multiplicación de sus divisores primos
# en lo anterior se basa el minímo común múltiplo
#al aplicar el m.c.m a 50, se obtiene que sus divisores primos son:2 y 5, por ende, sus divisores son 2, 5, 25 y 10
#(aunque también el mismo 50 y el 1)
x:int=1
def divisores(n:int,x:int):
  if (n<=50 and n>=2):
    print("los divisores del número",n,"son:")
    while(x<=n):
      r:int= n/x#aquí se dividira a n por todos los números hasta n
      if (n%x==0): print(r)#aquí se imprimiran solo los divisores, ya que solo estos dan divisiones exactas
      x=x+1
  else:
    print("introduzca solo números entre 2 y 50")

if __name__ =="__main__":
  n=int(input("ingrese un número entre 2 y 50:"))
  divisores(n,x)