#O código lê notas dos alunos até que o usuário digite -1, 
# desconsidera valores inválidos e calcula a média apenas das notas válidas, exibindo o resultado ao final.


media = 0
contador = 0
notas=0
while True:
  notas = int(input('Digite a nota do aluno: '))
  print (notas)
  if (notas < 0 or notas > 10) and notas!=-1:
    continue
  elif notas == -1:
    break
  else:
    media += notas
    contador += 1

if contador > 0:
    media /= contador
    print(f'A média dos alunos é {media}')
else:
    print('Nenhuma nota válida foi registrada.')
