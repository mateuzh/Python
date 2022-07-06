#Código para ler quantos números o usuário quiser com flag de parada sendo "999" utilizando break

n = s = q = 0
while True:
    n = int(input('Digite um valor [999 encerra o programa]: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'A soma dos {q} valores digitados foi {s}')