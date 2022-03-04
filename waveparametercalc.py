from Math import PI

VELOCIDADE = 3.8 * 10^8

def main():
  menu_principal()

  
def menu_principal():
  print('''            MENU
  =========================
  1 - Comprimento de onda
  2 - Frequência
  3 - Número de onda
  4 - Frequência angular
  =========================
        ''')
  print()
  
  
  option = int(input('Qual parâmetro de onda será a entrada?\n'))
 

  if option == 1:
    comprimento_de_onda()
  elif option == 2:
    frequencia()
  elif option == 3:
    numero_de_onda()
  elif option == 4:
    frequencia_angular()
  
  
def comprimento_de_onda():
   print('comprimento_de_onda')
def numero_de_onda():
  print('numero_de_onda')
  comp_onda = (2*PI) / valor

  
def frequencia():
  print('valor')
  comp_onda = calc_comprimento_de_onda(valor)
  freq_angular = calc_frequencia_angular(valor)

  
def frequencia_angular():
 print('frequencia_angular')

def calc_frequencia_angular(valor):
 return 2*PI*valor

def calc_comprimento_de_onda(frequencia):
  comp_onda = VELOCIDADE/frequencia
  return comp_onda
  

main() 
