def media(soma, cont):
    if soma != 0:
        return soma / cont
    else:
        return 0

#Função Principal
def main():
    cont = 0
    soma = 0
  #Enquanto a senteça for verdadeiro (True) ele se repete
    while True:
        qtd = int(input())
    
    #se o número digitado for terminado em zero, encerra o bloco de repetição.
        if qtd == 0:
            break
        soma += qtd
        cont += 1
  #media dos números
    m = media (soma,cont)
    if m != 0:
        print(f'{m:.2f}')

if __name__=='__main__':
  main()