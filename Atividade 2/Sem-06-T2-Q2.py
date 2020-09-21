def main():
  cont = 0
  soma = 0
  maior = 0
  menor = 0
  while True:
    idade = int(input('Digite sua idade: '))
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

  print(f'Ao todo foram {cont} pessoas')
  print(f'A media da idade foi {media}')
  print(f'A maior idade foi {maior}')
  print(f'A menor idade foi {menor}')

if __name__ == '__main__':
  main()