menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito:'))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        
        else:
            print('Não foi possível realizar essa operação: o valor informado é inválido.')
        
    elif opcao == 's':
        
        valor = float(input('Informe o valor do saque: '))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação falhou! Você não possui saldo suficiente para essa operação.')
        
        elif excedeu_limite:
            print('Operação falhou! O valor de saque excede o limite permitido.')
            
        elif excedeu_limite_saques:
            print('Operação falhou! Você já realizou as 3 operações de saques diárias permitidas.')
            
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            
        else:
            print('Não foi possível realizar essa operação: o valor informado é inválido.')
                    
    elif opcao == 'e':
        print('\n============================Extrato============================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}\n')
        print('=================================================================')
        
        
    elif opcao == 'q':
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')