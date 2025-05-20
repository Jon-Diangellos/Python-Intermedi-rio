#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo


n1 = int(input("Digite um número: "))

if n1 <= 1:
    print("O número não é primo.")
else:
    for x in range(2, n1):
        if n1 % x == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")