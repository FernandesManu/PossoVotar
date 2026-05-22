usuario_nasc = int(input('Qual o ano do seu nascimento?'))
ano_atual = 2026

calculo = ano_atual - usuario_nasc

print(f'hoje você tem {calculo} anos')

idade_votar = 16

if calculo >= idade_votar:
    print('pode votar')
else:
    print('ainda não pode votar')
