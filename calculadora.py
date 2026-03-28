
#crie uma calculadora foda
import math

history = []

def show_menu():
  print('\n === A CALCULADORA TOP ===')
  print('1 - Soma')
  print('2 - Subtração')
  print('3 - Multiplicação')
  print('4 - Divisão')
  print('5 - Potenciação')
  print('6 - Raiz Quadrada')
  print('7 - Seno')
  print('8 - Cosseno')
  print('9 - Tangente')
  print('10 - Ver Histórico')
  print('0 - Sair')

def get_numbers(two=True):
  if two:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    return a, b
  else:
    a = float(input('Digite o número: '))
    return a

while True:
  show_menu()
  choice = input('Escolha uma opção: ')

  if choice == '0':
    print('Saindo 😔')
    break

  elif choice == '1':
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    print('resultado: ', a + b)
    history.append(f"{a} + {b} = {result}")


  elif choice == '2':
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    print('resultado: ', a - b)
    history.append(f"{a} - {b} = {result}")

  elif choice == '3':
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    print('resultado: ', a * b)
    history.append(f"{a} * {b} = {result}")


  elif choice == '4':
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    print('resultado: ', a / b)

    if b == 0:
      print('Não é possível dividir por zero!')
    else:
      print('resultado: ', a / b)
    history.append(f"{a} / {b} = {result}")


  elif choice == '5':
    a = float(input('Base: '))
    b = float(input('Expoente: '))
    result = a ** b
    print('resultado: ', result)
    history.append(f"{a} ^ {b} = {result}")

  elif choice == '6':
    a = float(input('Número: '))

    if a < 0:
      print('Não é possível calcular a raiz quadrada de um número negativo!')
    else:
      result = math.sqrt(a)
      print('resultado: ', result)
      history.append(f"√{a} = {result}")

  elif choice == '7':
    a = float(input('Ângulo: '))
    result = math.sin(math.radians(a))
    print('resultado: ', result)
    history.append(f"sin({a}) = {result}")

  elif choice == '8':
    a = float(input('Ângulo: '))
    result = math.cos(math.radians(a))
    print('resultado: ', result)
    history.append(f"cos({a}) = {result}")

  elif choice == '9':
    a = float(input('Ângulo: '))
    result = math.tan(math.radians(a))
    print('resultado: ', result)
    history.append(f"tan({a}) = {result}")

  elif choice == '10':
    print('\n==== Histórico =====')
    for item in history:
      print(item)