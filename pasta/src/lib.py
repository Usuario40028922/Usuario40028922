import os

def clean():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux e macOS
        os.system('clear')

def printes(lista):
   for x in lista:
      print(x, end="\n")
      input
   


def nascer_dic(largura, altura):
  alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  dicionario = {}

  for x in range(altura):
    key = alfabeto_maiusculo[x]
    dicionario[key] = "~" * largura

  return dicionario




def mostrar_dic(largura, altura):
  alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  print("  1", end=" ")
  for x in range(largura - 1):
    print(f"{x + 2}", end=" ")
  print()

  v = "~ "

  for y in range(altura):
    print(f"{alfabeto_maiusculo[y]} {v * largura}")


if __name__ == '__main__':
  dicionario = nascer_dic(10, 10)
  print(dicionario)
  mostrar_dic(10, 10)
