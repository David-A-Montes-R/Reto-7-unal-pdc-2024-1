# imprimir un listado con los números del 1 al 100 cada uno con su respectico cuadrado
a:int=1
def cuadrados(a:int):
  while(a<=100):
    print("el número solicitado es:",a,"cuyo respectivo cuadrado es:",a**2)
    a= a+1

if __name__=="__main__":
  c=cuadrados(a)