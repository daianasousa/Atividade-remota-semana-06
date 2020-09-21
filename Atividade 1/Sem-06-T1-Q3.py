def maior_menor():
    cont = 0
    
    while True:
        numero = int(input('Digite um número: '))
    
    
        if numero == 0: break


        if cont == 0 and numero != 0:
            maior = numero
            menor = numero

        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        cont += 1
    return maior , menor  

def main():
    maior, menor = maior_menor()
    print(maior)
    print(menor)

if __name__== '__main__':
  main()
