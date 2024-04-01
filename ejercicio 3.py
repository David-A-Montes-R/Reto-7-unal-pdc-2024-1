#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural >= 2 dado 

def pares_mayores_2(a:int):
  if (a>=2):
    if a%2==0:
      print(a)
      while(a>2):
        print(a-2)
        a=a-2
    else:
      a=a-1
      print(a)
      while(a>2):
        print(a-2)
        a=a-2
  else:
    print("introduzca solo números naturales mayores o iguales a 2")

if __name__=="__main__":
  a= int(input("introduzca un número natural mayor o igual a 2:"))
  pm2=pares_mayores_2(a)
