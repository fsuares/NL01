from math import pi
from time import sleep

VELOCIDADE = (3 * (10 ** 8))


def menu_resposta(resposta):
    chaves = resposta.keys()
    print("Respostas")
    respostas_print = []
    for chave in chaves:
        resposta_frase = f"{str(chave).replace('_', ' ').title()} - {resposta[chave]}"
        respostas_print.append(resposta_frase)

    for respostas in respostas_print:
        print(respostas)


def calculos_gerais(comp_onda=None, freq=None, freq_ang=None, numero_de_onda=None):
    comp_onda = calcular_comprimento_de_onda(
        numero_de_onda=numero_de_onda) if numero_de_onda is not None else comp_onda

    # Calcular frequencia
    frequencia = freq or calcular_frequencia(
        comprimento_onda=comp_onda, freq_angular=freq_ang)
    # Calcular comprimento de onda
    comprimento_onda = comp_onda or calcular_comprimento_de_onda(
        frequencia=frequencia, numero_de_onda=numero_de_onda)
    # Calulcar nº de onda
    k = numero_de_onda or calcular_número_de_onda(comprimento_onda)
    # Calcular freq angular
    freq_angular = freq_ang or calulcar_frequencia_angular(frequencia)

    resposta = {
        'comprimento_de_onda': comprimento_onda,
        'frequencia': frequencia,
        'frequencia_angular': freq_angular,
        'numero_de_onda': k,
    }

    menu_resposta(resposta=resposta)


def comprimento_de_onda():
    comp_onda = float(input("Digite o comprimento de onda em metro: "))

    calculos_gerais(comp_onda=comp_onda)


def frequencia():
    freq = float(input("Digite a frequência em Hz: "))

    calculos_gerais(freq=freq)


def numero_de_onda():
    k = float(input("Digite o número de onda em rad/m: "))

    calculos_gerais(numero_de_onda=k)


def frequencia_angular():
    freq_angular = float(input("Digite a frequencia angular em rad/s: "))

    calculos_gerais(freq_ang=freq_angular)


def calcular_comprimento_de_onda(frequencia, numero_de_onda=None):
    comp_onda = (
        VELOCIDADE/frequencia) if numero_de_onda is None else 2*pi/numero_de_onda
    return comp_onda


def calulcar_frequencia_angular(frequencia):
    freq_ang = 2*pi*frequencia
    return freq_ang


def calcular_número_de_onda(comprimento_onda):
    k = (2*pi) / comprimento_onda
    return k


def calcular_frequencia(comprimento_onda, freq_angular=None):
    freq = (VELOCIDADE /
            comprimento_onda) if freq_angular is None else (freq_angular / 2*pi)
    return freq


def calc_campo_eletrico():
    camp_eletrico = int(
        input("Digite o valor do campo elétrico (em inteiros): "))

    campo_magnetico = camp_eletrico / VELOCIDADE

    print(f'Campo Magnético: {campo_magnetico}')


def cacl_campo_magnetico():
    camp_magnetico = float(input("Digite o valor do campo magnético: "))
    campo_eletrico = camp_magnetico * VELOCIDADE

    print(f'Campo Magnético: {campo_eletrico}')


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

    elif option == 5:
        calc_campo_eletrico()

    elif option == 6:
        cacl_campo_magnetico()
