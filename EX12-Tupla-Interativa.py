# O código permite que o usuário digite 8 números, 
# armazena-os em uma tupla e mostra: o maior número, 
# o menor número e quantas vezes o número 9 foi digitado.

numeros = ()

for i in range(8):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros += (num,)
            break
        except ValueError:
            print("Valor inválido! Por favor, digite um número inteiro.")

print("\nAnálise dos números:")
print(f"Você digitou: {numeros}")
print(f"O maior número é: {max(numeros)}")
print(f"O menor número é: {min(numeros)}")
print(f"O número 9 apareceu {numeros.count(9)} vezes.")
