import math


def apart(txt):
    size = 54
    print('=' * size)
    print(f'{txt:^{size}}')
    print('=' * size)


def select(val):
    while True:
        try:
            val = float(input(f'Digite o valor de {val.title()} na equação: '))
        except (ValueError, TypeError):
            print('\033[31mValor Inválido, tente novamente.\033[m')
        else:
            break
    return val


def bhaskara(a, b, c):
    apart('Resolução da Equação')
    delt = (b ** 2) - (4 * a * c)

    if delt < 0:
        print(f'\033[31;1mA equação não possui raízes reais (Δ < 0).\033[m')
        print(f'\033[97;1mValor de Δ = \033[m {delt}')

    if delt == 0:
        print(f'\033[33;1mA equação possui duas raízes reais e iguais (Δ = 0).\033[m')
        print(f'\033[97;1mValor de Δ = \033[m {delt}')
        nume_x1_x2 = -b
        den_x1_x2 = (2 * a)
        x1 = nume_x1_x2 / den_x1_x2
        x2 = nume_x1_x2 / den_x1_x2
        print(f'\033[97;1mValor de x¹ =\033[m {nume_x1_x2}/{den_x1_x2} = {x1}')
        print(f'\033[97;1mValor de x² =\033[m {nume_x1_x2}/{den_x1_x2} = {x2}')

    if delt > 0:
        print(f'\033[36;1mA equação possui duas raízes reais e distintas (Δ > 0).\033[m')
        print(f'\033[97;1mValor de Δ = \033[m {delt}')

        nume_x1 = (-b + math.sqrt(delt))
        den_x1 = (2 * a)
        x1 = nume_x1 / den_x1

        nume_x2 = (-b - math.sqrt(delt))
        den_x2 = (2 * a)
        x2 = nume_x2 / den_x2

        print(f'\033[97;1mValor de x¹ =\033[m {nume_x1}/{den_x1} = {x1}')
        print(f'\033[97;1mValor de x² =\033[m {nume_x2}/{den_x2} = {x2}')
