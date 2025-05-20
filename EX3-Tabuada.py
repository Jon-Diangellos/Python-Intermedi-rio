num=int(input("Digite o numero de qual tabuada deseja: "))
n2=int(input("Digite ate qual numero deseja multiplicar: "))

for x in range(1,n2+1):
  print(f'{num} x {x} = {num*x}')