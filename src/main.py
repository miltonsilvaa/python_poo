from frota import *

def operar_carro(carro : Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro1.ligar()
    elif op == 2:
        carro1.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro1.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)

if __name__ == "__main__":
    print('Cadastre o carro 1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Informe o nível do tanque: '))
    cm = float(input('Consumo médio: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    print('Cadastre o carro 2')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Informe o nível do tanque: '))
    cm = float(input('Consumo médio: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    '''
    Controlando o carro até ele atingir 600 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600 and \
            (carro1.tanque > 0 or carro2.tanque > 0):
        try:
            op_carro = 0
            while op_carro not in (1,2):
                op_carro = int(input('Qual carro vai usar [1,2]?'))

            if op_carro == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)
    try:
        carro1.desligar()
        carro2.desligar()
    except Exception as e:
        print('Erro!')
        print(e)
    if carro1.odometro > carro2.odometro:
        print(carro1)
    else:
        print(carro2)

