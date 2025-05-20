#O código lê 10 números do usuário e conta quantos são pares e quantos são ímpares, exibindo os totais ao final.

impar=0
par=0

for x in range(10):
  num=int(input(f'Digite o {x+1}° número:'))
  if num%2==0:
    par+=1
  else:
    impar+=1

print(f'A quantidade de números pares é {par}')
print(f'A quantidade de números ímpares é {impar}')