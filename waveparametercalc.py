

from functionsWave import *



VELOCIDADE = 3.8 * 10**8


def main():
  while True:
    choice = int(input("\n1 - Iniciar programa\n2 - Encerrar programa\n\n"))
    if choice == 1:
      menu_principal()
      
    elif choice == 2:
      print("Encerrando...")
      sleep(1)
      break
    
    else:
      print("\nErro.\nFavor entrar com uma opção válida.\n")
      sleep(1)
  
main()


main() 
