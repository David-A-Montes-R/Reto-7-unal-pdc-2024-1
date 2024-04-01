# imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000
a:int= 1
b:int= 2
def pares_e_impares(a:int,b:int):
  print("los números impares desde 1 hasta 999 son:")
  print(a)
  while (a<999):
    print(a+2)
    a=a+2
  print("los números pares desde 2 hasta 1000 son:")
  print(b)
  while (b<1000):
    print(b+2)
    b=b+2

if __name__ == "__main__":
  pei=pares_e_impares(a,b)