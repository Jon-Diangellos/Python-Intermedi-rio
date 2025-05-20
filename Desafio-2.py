#O código lê o ano de nascimento de 7 pessoas, calcula suas idades 
# e conta quantas são maiores ou menores de 18 anos, exibindo os totais ao final.

ano= 2025
maiores = 0
menores = 0

for i in range(1,8):
    ano_nasc = int(input(f"me fale o ano de nascimento da {i}º pessoa: "))
    idade = ano - ano_nasc

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Total de maiores de idade: {maiores}")
print(f"Total de menores de idade: {menores}")