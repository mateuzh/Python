from random import randint


def maior(* num):
    for i, v in enumerate(num):
        if i == 0 or v > maior:
            maior = v
    print(f'Foram passados {len(num)} números ')
    print(f'Os valores passados foram {num} e o maior valor entre eles é {maior}')

print(f'-=' * 20)
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
