from modules.eleitoral import verificar_voto

ano_nasc = int(input('Qual o ano do seu nascimento? '))

apto, resultado = verificar_voto(ano_nasc)
print(resultado)
