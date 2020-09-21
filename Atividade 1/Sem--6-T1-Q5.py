def ano_mes(s, d):
    mes = 10
    ano = 2016

    while not d > s:
        d += (15 / 100) * d

        if mes <= 12:
            if mes == 3:
                aumento = (5 / 100) * s
                s += aumento
        
        else:
            mes = 1
            ano += 1
        
        mes += 1

    return mes , ano
def main():
    salario = float(input())
    divida = float(input())

    if salario != 0 and divida != 0:
        mes, ano = ano_mes(salario, divida)

        print(f'{mes}/{ano}')


if __name__ == '__main__':
  main()