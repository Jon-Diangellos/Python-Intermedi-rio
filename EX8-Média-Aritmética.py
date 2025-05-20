#Faça um programa que calcule o mostre a média aritmética de N notas


n = int(input("Digite a quantidade de notas: "))
notas = []
for i in range(n):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
media = sum(notas) / n
print(f"A média aritmética das notas é: {media:.2f}")