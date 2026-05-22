def verificar_voto(ano_nasc):
    ano_atual = 2026
    idade_usuario = ano_atual - ano_nasc

    if idade_usuario >= 16:
        idade_apta = True
        return f"Você tem idade para votar, pois tem {idade_usuario} anos."
    else:
        idade_apta = False
        return False, f"Você não tem idade para votar, pois tem {idade_usuario} anos."
