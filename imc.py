peso = float(input('Digite seu Peso: '))
print('-='*20)
altura = float(input('Digite sua Altura: '))
print('-='*20)
imc = peso / (altura * altura)
print(f'{imc:.2f}')
if imc < 18.5:
  print('MAGREZA')
elif imc >= 18.5 and imc <= 24.9:
  print('NORMAL')
elif imc >= 25.0 and imc < 29.9:
  print('-='*20)
  print('SOBREPESO')
  print('-='*20)
elif imc >= 30.0 and imc <= 39.9:
  print('-='*20)
  print('OBESIDADE')
  print('-='*20)
elif imc > 40.0:
  print('-='*20)
  print('OBESIDADE GRAVE')
  print('-='*20)
