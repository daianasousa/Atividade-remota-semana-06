def texto_1():
  return f'1 - Olá. Como vai?'
def texto_2():
  return f'2 - Vamos estudar mais.'
def texto_3():
  return f'3 - Meus Parabéns!'
def texto_4():
  return f'0 - Fim de Serviço'
def texto_5():
  return f'Opção inválida.'


def main():
    while True:
        print('''
OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
        opcao = int(input())

        if opcao == 1:
            print(texto_1())
        elif opcao == 2:
            print(texto_2())
        elif opcao == 3:
            print(texto_3())
        elif opcao == 0:
          print(texto_4())
          if opcao == 0: break  
        else:
          print(texto_5())

if __name__ == '__main__':
  main()
      