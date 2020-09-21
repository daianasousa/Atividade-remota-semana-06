def main():
  print('''
  CÓDIGO   PRODUTO          PREÇO (R$)
  H        Hamburger        5.50
  C        Cheeseburger     6.80
  M        Misto Quente     4.50
  A        Americano        7.00
  Q        Queijo Prato     4.00
  X        PARA TOTAL DA CONTA
  ''')
  soma = 0
  while True:
    codigo = input('Código: ').upper()[0]
    if codigo == 'H':
      preco = 5.50 
      soma += preco
    elif codigo == 'C': 
      preco = 6.80 
      soma += preco
    elif codigo == 'M': 
      preco = 4.50 
      soma += preco
    elif codigo == 'A': 
      preco = 7.00 
      soma += preco
    elif codigo == 'Q': 
      preco = 4.00 
      soma += preco
    elif codigo == 'X':
      total = soma
      if codigo == 'X': break
    else:
      print('Opção inválida')
  print(f'O total a pagar é de {total:.2f}')

if __name__ == '__main__':
  main()