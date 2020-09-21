def main():
  soma = 0
  while True:
    num = int(input('Digite um número: '))
    soma += num
    if num == 0: break
  print(soma)

if __name__ == '__main__':
  main()
