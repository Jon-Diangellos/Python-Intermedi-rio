#O código simula uma votação entre 3 candidatos, registra os votos de um número definido de eleitores e
# ao final, exibe o vencedor ou informa se houve empate.


import time
eleitores= int (input('Digite o número total de eleitores que vão votar:'))
cand1=str (input('Digite o nome do primeiro candidato:'))
cand2=str (input('Digite o nome do segundo candidato'))
cand3=str (input('Digite o nome do terceiro candidato:'))
res_cand1= 0
res_cand2= 0
res_cand3= 0
for x in range(1, eleitores+1):
  while True:
    print (f'''Qual o seu candidato?
      -Digite 12 para {cand1},
      -Digite 13 para {cand2}
      -Digite 14 para {cand3}''')
    voto= int (input('Digite o número do seu candidato:'))
    match voto:
      case 12:
        res_cand1 +=1
        print ('Voto computado!')
        time.sleep (3)
        break
      case 13:
        res_cand2 +=1
        print ('Voto computado!')
        time.sleep (3)
        break
      case 14:
        res_cand3 +=1
        print ('Voto computado!')
        time.sleep (3)
        break
      case _:
        print ('Opção inválida, refaça o procedimento')
if res_cand1 > res_cand2 and res_cand1 > res_cand3:
  print (f'O vencedor foi {cand1} com {res_cand1} votos')
elif res_cand2 > res_cand1 and res_cand2 > res_cand3:
  print (f'O vencedor foi {cand2} com {res_cand2} votos')
elif res_cand3 > res_cand1 and res_cand3 > res_cand2:
  print (f'O vencedor foi {cand3} com {res_cand3} votos')
elif res_cand1 == res_cand2 and res_cand1 > res_cand3:
  print (f'Empate entre {cand1} e {cand2}')
elif res_cand1 == res_cand3 and res_cand1 > res_cand2:
  print (f'Empate entre {cand1} e {cand3}')
else:
  res_cand2 == res_cand3 and res_cand2 > res_cand1
  print (f'Empate entre {cand2} e {cand3}')