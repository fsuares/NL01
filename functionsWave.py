

from math import pi
from time import sleep


def menu_resposta(resposta):
    chaves = resposta.keys()
    print("Respostas")
    respostas_print = []
    i = 0
    for chave in chaves:
        respostas_print[i] = f"{str(chave).replace('_', ' ').title()} - {resposta[chave]}"
        i += 1

    for respostas in respostas_print:
        print(respostas)


def comprimento_de_onda():
    comp_onda = float(input("Digite o comprimento de onda em metro: "))
    # Calcular frequencia
    freq = calcular_frequencia(comp_onda)
    # Calulcar nº de onda
    k = calcular_número_de_onda(comp_onda)
    # Calcular freq angular
    freq_ang = calulcar_frequencia_angular(freq)

    resposta = {
        frequencia: freq,
        numero_de_onda: k,
        frequencia_angular: freq_ang,
    }

    menu_resposta(resposta=resposta)


def calulcar_frequencia_angular(frequencia):
    freq_ang = 2*pi*frequencia
    return freq_ang


def calcular_número_de_onda(comprimento_onda):
    k = (2*pi) / comprimento_onda
    return k


def calcular_frequencia(comprimento_onda):
    freq = (3*10^8)/ comprimento_onda
    return freq



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


