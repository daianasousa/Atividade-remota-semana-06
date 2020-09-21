print('''
Conceito       Nota
A              >= 8.5
B              >= 7.0
C              >= 5.0
D              >= 4              
E              >= 0
''')

while True:
  nota = float(input("Digite a nota entre 0 e 10: "))

  if nota >= 8.5 and nota <= 10:
    conceito = 'A'
    print(conceito)
  elif nota >= 7.0 and nota < 8.5:
    conceito = 'B'
    print(conceito)
  elif nota >= 5.0 and nota < 7.0:
    conceito = 'c'
    print(conceito)
  elif nota >= 4 and nota < 5.0:
    conceito = 'D'
    print(conceito)
  elif nota >= 0 and nota < 4.0:
    conceito = 'E'
    print(conceito)
  else:
    print('Nota Inválida.')