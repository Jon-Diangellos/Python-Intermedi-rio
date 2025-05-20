#O código solicita dois números distintos, imprime todos os valores entre eles 
# (inclusive) e mostra a soma dos dois números e a soma de todo o intervalo.


num1=int (input('Digite um número:'))
num2=int (input('Digite um número'))
soma=0
while num1==num2:
  print('Os números são iguais, tente novamente')
  num1=int (input('Digite um número:'))
  num2=int (input('Digite um número'))

if num1<num2:
  for x in range(num1, num2+1):
    print(x, end= ' ')
    soma+=x
else:
  for x in range(num2, num1+1):
    print(x, end= ' ')
    soma+=x

print(f'a soma dos números é {num1+num2} e a soma dos intervalos sao {soma} ')