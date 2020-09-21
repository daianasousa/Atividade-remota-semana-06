def main():
  cont = 0
  soma = 0
  maior = 0
  menor = 0
  while True:
    idade = int(input())
    if idade == 0: break
    cont += 1
    soma += idade
    media = soma / cont

    if cont == 1:
      maior = idade
      menor = idade

    else:
      if idade > maior:
        maior = idade
      elif idade < menor:
        menor = idade

  print(f'{cont}')
  print(f'{media}')
  print(f'{menor}')
  print(f'{maior}')

if __name__ == '__main__':
  main()
