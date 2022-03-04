

from math import pi
from time import sleep


def comprimento_de_onda():
  print('comprimento_de_onda')


def numero_de_onda():
  print('numero_de_onda')
  comp_onda = (2*pi) / valor


def frequencia():
  print('valor')
  comp_onda = calc_comprimento_de_onda(valor)
  freq_angular = calc_frequencia_angular(valor)


def frequencia_angular():
  print('frequencia_angular')


def calc_frequencia_angular(valor):
  return 2*pi*valor


def calc_comprimento_de_onda(frequencia):
  comp_onda = VELOCIDADE/frequencia
  return comp_onda


def menu_principal():
  sleep(1)
  print('\nQual parâmetro de onda será a entrada?\n')
  print("""                 OPÇÕES
---------------------------------------
|       1 - Comprimento de onda       |
|       2 - Frequência                |
|       3 - Número de onda            |
|       4 - Frequência angular        |
|       5 - Campo elétrico            |
|       6 - Campo magnético           |
---------------------------------------
""")

  option = int(input("Escolha: "))

  if option == 1:
    comprimento_de_onda()

  elif option == 2:
    frequencia()

  elif option == 3:
    numero_de_onda()

  elif option == 4:
    frequencia_angular()


