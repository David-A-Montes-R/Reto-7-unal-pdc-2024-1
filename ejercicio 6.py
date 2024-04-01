#Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
m:int=90
def adivinador(n:str,m:int):
  if n=="<":
    print("no se pueden usar números mayores a 100, por favor intente de nuevo")
  else:
    while n==">" and m>0:
      print("¿es el número",m,"mayor, menor o igual a su número escogido?")
      n=input(":")
      m=m-10
      if not n==">": break
      if m==10: m=m-9
    m=m+10
    if n=="<":
      m=m+1
      while n=="<":
        print("¿es el número",m," menor o igual a su número escogido?")
        n=input(":")
        m=m+1
        if m>100: break
        if n==">":
          print("tal vez se equivocó de signo, por favor intente de nuevo")
        if n=="=":break
      m=m-1
      print("su número escogido es el número",m)
    else:
        print("su número escogido es el número",m)

if __name__=="__main__":
  print("por favor solo introduzca respuestas de <, > o =")
  n=input("¿El número 100 es mayor o igual a su número escogido?: ")
  adivinador(n,m)