#O código lê dados de 7 pessoas, identifica o homem mais velho, conta quantas mulheres têm menos de 20 anos e 
# calcula a média das idades (somando apenas as dos homens mais velhos). Depois, exibe essas informações.


soma_idade = 0
M_nova =0
H_velho =0
for x in range(1,8):
    print(f'Dados da {x}º pessoa ')
    nome = input('nome: ')
    idade= int(input('idade: '))
    sexo = input('sexo (H/M): ')
    if idade > H_velho and (sexo == 'H' or sexo == 'h'):
        H_velho = idade
        nome_velho = nome
        soma_idade += idade
    if (sexo == 'M' or sexo == 'm') and idade < 20:
        M_nova +=1

print(f'''    O nome do homem mais velhor do grupo é {nome_velho},
    A media de idade e {soma_idade /7:.2f}.
    A quantidade de mulheres com menos de 20 anos è : {M_nova} pessoa(s)''')