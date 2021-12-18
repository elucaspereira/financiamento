print('-='*35)
print('Banco Vulcano')
print('-='*35)
print('\033[7;31mBem vindo ao Banco Vulcano\033[m')
print('\033[1;36mSimulaçao de finaciamento residencial\033[m')
nome = str(input('\033[1;36mDigite seu nome:\033[m')).strip().title()
email = str(input('\033[1;36mDigite seu e-mail:\33[m ')).strip()
cpf = str(input('\033[1;36mDigite seu CPF (somente numeros):\033[m ')).strip()
cpf_format = '{}.{}.{}-{}'.format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:])
celular = str(input('\033[1;36mDigite seu celular:\033[m ')).strip()
cel = celular
formatcel = '({}) {}-{}'.format(cel[:2],cel[2:7],cel[7:11])
valor = float(input('\033[1;36mQual o valor total do financiamento:\033[m'))
salario = float(input('\033[1;36mDigite sua renda mensal R$:\033[m '))
parcelas = int(input('\033[1;36mTotal de prestações desejada:\033[m'))
juros = valor * 3/100 * parcelas
total_juros = (valor + juros) / parcelas
prestacao = total_juros
minimo = salario * 30 / 100
print('Olá cliente {}'.format(nome))
print(email)
print(formatcel)
print(cpf_format)
print('O valor das parcelas será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('\033[1;32mSeu cadastro segue todas as nossas regras e seu financiamento está aprovado\033[m')
else:
    print('\033[1;31mInfelizmente sua renda é inferior as normas do banco e o finaciamento foi Negado\033[m')
print('\033[1;36mAtendimento Finalizado\033[m')
