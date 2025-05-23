# O código coleta e valida informações pessoais do usuário 
# (nome, idade, sexo, salário e estado civil), 
# garantindo que cada dado atenda aos critérios exigidos antes de exibir um resumo completo.


nome = ""
idade = 0
salario = 0
sexo = ""
estado_civi = ""
while len(nome)<=3:
  nome = str(input("Digite seu nome: "))
  if len(nome)<=3:
    print("nome invalido!")
  else:
    print("nome registrado!")
while idade <= 0 or idade > 150:
  idade = int(input("Digite sua idade: "))
  if idade < 0 or idade > 150:
    print("idade invalida!")
  else:
    print("idade registrada!")
while sexo.lower() != "f" and sexo.lower() != "m":
  sexo = str(input("Digite seu sexo: "))
  if sexo.lower() != "f" and sexo.lower() != "m":
    print("sexo invalido!")
  else:
    print("sexo registrado!")
while salario <= 0 :
  salario = float(input("Digite seu salario: "))
  if salario <= 0 :
    print("salario invalido!")
  else:
    print("salario registrado!")

while estado_civi.lower() != "s" and estado_civi.lower() != "c" and estado_civi.lower() != "v" and estado_civi.lower() != "d":
  estado_civi = str(input("Digite seu estado civil: "))
  if estado_civi.lower() != "s" and estado_civi.lower() != "c" and estado_civi.lower() != "v" and estado_civi.lower() != "d":
    print("estado civil invalido!")
  else:
    print("estado civil registrado!")

sexofinal=''
if sexo == 'm':
  sexofinal="masculino"
else:
  sexofinal="feminino"

stad_final=""
if estado_civi == 's':
  stad_final="solteiro"
elif estado_civi == 'c':
  stad_final="casado"
elif estado_civi == 'v':
  stad_final="viuvo"
elif estado_civi == 'd':
  stad_final="divorciado"

print(f'''nome: {nome}
idade: {idade}
sexo: {sexofinal}
salario: {salario}
estado civil: {stad_final}
''')
