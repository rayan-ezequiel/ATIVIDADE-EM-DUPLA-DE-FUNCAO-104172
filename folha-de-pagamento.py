import os
os.system('cls' if os.name == 'nt' else 'clear')

print('$ $ $ FOLHA DE PAGAMENTO $ $ $')


def login():
    matricula = int(input('Digite sua matricula: '))
    senha = input('Digite sua senha: ')
    return matricula, senha


def entradas():
    while True:
        salario_base = float(input('Digite o salário base: '))
        
        #DEPENDENTES
        dependentes = int(input('Quantos Dependentes ? '))
        
        #SALARIO BASE TRANSPORTE E VALE REFEICAO
        if salario_base <= 0:
            print('VALOR INVÁLIDO')
            continue
        else:
            print('VALOR ACEITO')
            valor_vale_refeicao = float(input('Digite o valor do vale refeição: R$ '))
            vale_transporte = input('Aceita VT  ? S / N ').upper()
            if vale_transporte == 'S':
                valor_vale_transporte = float(input('VALE TRANSPORTE INCLUSO\nINSIRA O VALOR: R$ '))
                desconto_vt = salario_base * 0.06
                if desconto_vt > valor_vale_transporte:
                    desconto_vt = valor_vale_transporte
            elif vale_transporte == 'N':
                print('VALE TRANSPORTE NAO INCLUSO')
                desconto_vt = 0
            else:
                print('VALOR INVÁLIDO')
                continue
        return salario_base, dependentes, valor_vale_refeicao, desconto_vt


def calcular_inss(salario_base):
    if salario_base <= 1621:
        valor_inss = salario_base * 0.075
    elif salario_base >= 1621.01 and salario_base <= 2902.84:
        valor_inss = salario_base * 0.090
    elif salario_base >= 2902.85 and salario_base <= 4354.27:
        valor_inss = salario_base * 0.12
    elif salario_base >= 4354.28 and salario_base <= 8475.55:
        valor_inss = salario_base * 0.14
    else:
        valor_inss = 8475.55 * 0.14
    return valor_inss


def calcular_irrf(salario_base, valor_inss, dependentes):
    base = salario_base - valor_inss - (189.59 * dependentes)
    
    if base <= 2428.80:
        print('ISENTO')
        imposto = 0
    elif base >= 2428.81 and base <= 2826.65:
        imposto = (base * 0.075) - 182.16
    elif base >= 2826.66 and base <= 3751.05:
        imposto = (base * 0.15) - 394.16
    elif base >= 3751.06 and base <= 4664.68:
        imposto = (base * 0.225) - 675.49
    elif base > 4664.68:
        imposto = (base * 0.275) - 908.73
    else:
        print('VALOR INVÁLIDO')
        imposto = 0
    return imposto


def calcular_vr(valor_vale_refeicao):
    desconto_vr = valor_vale_refeicao * 0.20
    return desconto_vr


def calcular_plano_saude(dependentes):
    desconto_do_plano = 150 * dependentes
    return desconto_do_plano


def contracheque(matricula, salario_base, valor_inss, valor_irrf, valor_vale_transporte, valor_vale_refeicao, plano_de_saude, total_de_descontos, valor_liquido):
    print(f'CONTRACHEQUE • MATRÍCULA {matricula}')
    print(f'Salário base                 R$ {salario_base:.2f}')
    print(f'(-) INSS                     R$ {valor_inss:.2f}')
    print(f'(-) IRRF                     R$ {valor_irrf:.2f}')
    print(f'(-) Vale-transporte          R$ {valor_vale_transporte:.2f}')
    print(f'(-) Vale-refeição            R$ {valor_vale_refeicao:.2f}')
    print(f'(-) Plano de saúde           R$ {plano_de_saude:.2f}')
    print('---------------------------------------------')
    print(f'Total de descontos           R$ {total_de_descontos:.2f}')
    print(f'SALÁRIO LÍQUIDO              R$ {valor_liquido:.2f}')


matricula, senha = login()
salario_base, dependentes, valor_vale_refeicao, valor_vale_transporte = entradas()
valor_inss = calcular_inss(salario_base)
valor_irrf = calcular_irrf(salario_base, valor_inss, dependentes)
valor_vale_refeicao = calcular_vr(valor_vale_refeicao)
plano_de_saude = calcular_plano_saude(dependentes)

total_de_descontos = valor_inss + valor_irrf + valor_vale_transporte + valor_vale_refeicao + plano_de_saude
valor_liquido = salario_base - total_de_descontos

contracheque(matricula, salario_base, valor_inss, valor_irrf, valor_vale_transporte, valor_vale_refeicao, plano_de_saude, total_de_descontos, valor_liquido)