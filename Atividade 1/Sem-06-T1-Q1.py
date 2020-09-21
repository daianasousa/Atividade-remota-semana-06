#Criei uma função para descobri a quantidade de anos
#d = deposito  t = taxa
def ano(d, dobro, t):
  ano = 0
  #Enquanto o meu valor for menor que o seu dobro, continuara a conta a quantidade de anos
  while d < dobro:
    a = (d * (t / 100)) + d
    d = a
    ano += 1
  return ano
#Criei a função Pricipal
def main():
  #Recebe o deposito inicial
  deposito = float(input("Digite o depósito inicial da sua poupança:R$ "))
  #recebe a taxa ao ano
  taxa = float(input("Digite a taxa de juros ao ano de sua poupança: "))
  dobro = deposito * 2
  #retorna a função ano
  qnt = ano(deposito,dobro, taxa )

  print(f'Em {qnt} anos você acumulou o valor esperado')


if __name__ == '__main__':
  main()