#O código lê 6 números do usuário e soma apenas os que forem pares, exibindo o total ao final.

soma=0
for x in range(6):
  n1=int(input("Digite qualquer numero: "))
  if n1%2==0:
    soma +=n1
print(f'A soma dos pares é {soma}')
