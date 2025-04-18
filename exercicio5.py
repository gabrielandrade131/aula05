soma = 0
for i in range(5):
    numero = float(input(f'Digite o {i+1}° número: '))
    soma += numero

media = soma / 5

print(f'A soma é {soma}')
print(f'A média é: {media}')