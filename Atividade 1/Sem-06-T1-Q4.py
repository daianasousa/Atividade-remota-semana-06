def main():
  num = int(input())
  inverso = 0
  while num > 0:
    inverso = (inverso * 10) + num % 10
    num//= 10
  print(inverso)

if __name__ == '__main__':
  main()