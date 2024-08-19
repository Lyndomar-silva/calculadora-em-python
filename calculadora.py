from regra_de_negócios import esolher_operação
from math import trunc

def calcular():
    operação = esolher_operação()

    numero_1 = int(input('Digite um numero:'))
    numero_2 = int(input('Digite um segundo numero:'))

    if operação == '+':
        soma = numero_1 + numero_2
        print(f'A soma dos numeros é {soma}')
    
    elif operação == '-':
        subtração = numero_1 - numero_2
        print(f'A subtração dos numeros é {subtração}')
    
    elif operação == 'x':
        multiplicação = numero_1 * numero_2
        print(f'A multiplicação dos numeros é {multiplicação}')
    else:
        if numero_1 == 0:
            if numero_2 == 0:
                print('Erro: 0 não pode ser divisivél por 0')
            else:
                print('Erro: divisão por 0 não é permitida')
        else:
            divisão = numero_1 / numero_2
            print(f'A divisão dos numeros é {trunc(divisão)} ')


calcular()
    
