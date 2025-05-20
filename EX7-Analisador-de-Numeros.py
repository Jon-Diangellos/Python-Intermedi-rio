# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


menor=0
maior=0
soma=0


n = int(input("Digite a quantidade de números: "))
numeros = []

for i in range(n):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)


print(f"O menor valor é: {menor:.0f}")
print(f"O maior valor é: {maior:.0f}")
print(f"A soma dos valores é: {soma:.0f}")