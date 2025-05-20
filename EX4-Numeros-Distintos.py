# O código solicita dois números diferentes e imprime todos os valores inteiros
# entre eles, em ordem crescente. Se os números forem iguais, pede que o usuário tente novamente.


num1=int (input('Digite um número:'))
num2=int (input('Digite um número'))

while num1==num2:
  print('Os números são iguais, tente novamente')
  num1=int (input('Digite um número:'))
  num2=int (input('Digite um número'))

if num1<num2:
  for x in range(num1, num2+1):
    print(x, end= ' ')
else:
  for x in range(num2, num1+1):
    print(x, end= ' ')