# en 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones.
# las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente.
#Desarrollar  un algoritmo para informar en que año la población el país B superara a la de A.

a:int=25000000
b:int=18900000
tc_a:float=0.02
tc_b:float=0.03
año:int=2022
def predicción(a:int,b:int,tc_a:float,tc_b:float,año:int):
  while(b<a):
    a= a+a*tc_a
    b= b+b*tc_b
    año= año+1
  print("el año en el que la población de B superará a la de A será:",año)
  print("A contará con una población de:",a,"habitantes y B con una población de:",b,"habitantes")

if __name__ == "__main__":
  p=predicción(a,b,tc_a,tc_b,año)