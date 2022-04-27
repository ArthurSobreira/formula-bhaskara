from FormulaBhaskaraFunctions import *


def main():
    apart('Fórmula de Bhaskara')

    while True:
        a = select('a')
        if a == 0:
            print('\033[31mValor inválido, lembre-se que se trata de uma equação do segundo grau.\033[m')
            continue
        break

    b = select('b')
    c = select('c')
    print('=' * 54)

    if (b == 0) or (c == 0):
        if (b == 0) and (c == 0):
            print('\033[32mEquação Imcompleta para B e C:\033[m', end=' ')
            print(f'{a}x² = 0')
        if (b == 0) and ((c > 0) or (c < 0)):
            print('\033[32mEquação Imcompleta para B:\033[m', end=' ')
            if c > 0:
                print(f'{a}x² + {c} = 0')
            if c < 0:
                c_temp = c * -1
                print(f'{a}x² - {c_temp} = 0')
        if (c == 0) and ((b > 0) or (b < 0)):
            print('\033[32mEquação Imcompleta para C:\033[m', end=' ')
            if b > 0:
                print(f'{a}x² + {b}x = 0')
            if b < 0:
                b_temp = b * -1
                print(f'{a}x² - {b_temp}x = 0')
    else:
        print('\033[32mEquação do Segundo Grau Completa:\033[m', end=' ')
        if (b > 0) and (c > 0):
            print(f'{a}x² + {b}x + {c} = 0')
        if (b < 0) and (c < 0):
            b_temp = b * -1
            c_temp = c * -1
            print(f'{a}x² - {b_temp}x - {c_temp} = 0')
        if (b < 0) and (c > 0):
            b_temp = b * -1
            print(f'{a}x² - {b_temp}x + {c} = 0')
        if (b > 0) and (c < 0):
            c_temp = c * -1
            print(f'{a}x² + {b}x - {c_temp} = 0')

    bhaskara(a, b, c)


if __name__ == '__main__':
    main()