# 1° - Função de criar o tabuleiro e guardar em uma variável.
# 2° - Função de mostrar o tabuleiro e outra para atualizar o tabuleiro.


import os

alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def clean():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux e macOS
        os.system('clear')

def printes(lista):
   for x in lista:
      print(x, end="\n")
      input()

def seu_terminal_aguenta():
  import os

  tamanho_terminal = os.get_terminal_size()

  largura = tamanho_terminal.columns

  # (3 + (8 * 2)) + (N * 3) = 140
  # 19 + (N * 3) = 140
  # (N * 3) = 140 - 19
  # N = 121 / 3
  # N = 40,3
  # 19 + (40 * 3) = 139
  # igual a 140 se a variavel for igual a 40,33333333333333

  a_partir_de_dez_soma_tres = (largura - 19) / 3
  formula = 3 + 16 + a_partir_de_dez_soma_tres * 3
  print(f"{tamanho_terminal}\nVocê só pode até uns {(10 + a_partir_de_dez_soma_tres) - 1}")

  print(largura, formula)
  # Tamanho em colunas (largura) e linhas (altura)



def nascer_dic(largura, altura, betoalfa):
  alfabeto_maiusculo = betoalfa

  dicionario = {}

  alfabeto = []
  num = 1

  for x in range(altura):
    if x > len(alfabeto_maiusculo) - 1:
      
      for y in range(len(alfabeto_maiusculo)):
        string = f"{alfabeto_maiusculo[y]}{num}"
        alfabeto.append(string)
      
      num += 1
      alfabeto_maiusculo += alfabeto
      print(alfabeto_maiusculo)

    key = alfabeto_maiusculo[x]
    dicionario[key] = "~" * largura

  return dicionario, alfabeto_maiusculo




def mostrar_dic(dicionario, betoalfa):
  alfabeto_maiusculo = betoalfa
  
  num = 1
  print(" ", end="")
  for x in dicionario.keys():
    print(f" {num}", end="")
    #print(f"{num}", end=" ")
    num += 1
  print()


  valor = len(dicionario['A'])
  v = "~"
  nada = " "
  print(f"\n")
  for z in range(len(dicionario.keys())):
    print(f"{alfabeto_maiusculo[z]}", end="")

    for y in range(valor):
      if z <= 25:
        if y < 9:
          print(f" {v}", end="")
          continue
        elif y >= 9:
          #if z 
          print(f"  {v}", end="")
          continue

      elif z > 25:
        if y < 9:
          print(f"{v}", end=" ")
          continue
        elif y >= 9:
          #if z 
          print(f" {v}", end=" ")
          continue
        
        

      #elif y > 100 and y < 1000:
          #print(f"{alfabeto_maiusculo[y]} {v}")
          #continue
      print(f" {v}", end="")
      v = "~"

    print()


if __name__ == '__main__':
  
  seu_terminal_aguenta()
  dicionario, alfabeto = nascer_dic(53, 53, alfabeto_maiusculo)
  print(len(alfabeto))
  print(".")
  mostrar_dic(dicionario, alfabeto)
