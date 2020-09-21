#Função Principal
def main():
  #Contadores
  cont = 0
  soma = 0
  #Enquanto a senteça for verdadeiro (True) ele se repete
  while True:
    qtd = int(input("Digite um número: "))

    #se o número digitado for terminado em zero, encerra o bloco de repetição.  
    if qtd == 0: break
    soma += qtd
    cont += 1 
  #media dos números
  media = soma / cont
  print(f'A média é {media:.2f}')

if __name__=='__main__':
  main()