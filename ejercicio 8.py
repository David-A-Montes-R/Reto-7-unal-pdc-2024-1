#implementar el algoritmo que muestre los números primos del 1 al 100. Nota: Use funciones

# vamos a hacerlo de una forma que saldrá, aunque puede ser un poquito trampa
# tras echar un repasito, es posible afirmar lo siguiente:
# si no se han encontrado divisores hasta la raíz cuadrada de un número:
#el número es primo
#aquí el máximo número es 100
#la raíz cuadrada de 100 es 10
#por ende, solo es necesario conocer si hay divisores de un número hasta 10
# y estos divisores solo pueden ser los números primos: 2,3,5 y 7
#(por esto ultimo digo que es medio trampa, y es que ya sabemos de antemano que 2, 3, 5 y 7 son primos)

def mult_2(n:int):
    if not(n%2==0) or n==2:
        return True
    else:
        return False
def mult_3(n:int):
    if not(n%3==0) or n<=3:
        return True
    else:
        return False
def mult_5(n:int):
    if not(n%5==0) or n<=5:
        return True
    else:
        return False
def mult_7(n:int):
    if not(n%7==0) or n<=7:
        return True
    else:
        return False

if __name__ == "__main__":
  n:int=2 # los números primos empiezan desde el 2 porque el 1 no es primo
  print("los números primos hasta el 100 son:")
  while (n<100):
    m2:bool=mult_2(n)
    m3:bool=mult_3(n)
    m5:bool=mult_5(n)
    m7:bool=mult_7(n)
    if m2==True and m3==True and m5==True and m7==True:
    #si el número no es multiplo ni de 2, ni de 3, ni de 5, ni de 7, será primo.
        print(n)
    n=n+1
