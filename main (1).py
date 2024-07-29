def rotacionar_texto(rotacoes, texto):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    texto_cifrado = ''

    for char in texto:
        if char.lower() in alfabeto:  # Verifica se é uma letra do alfabeto
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            # Calcula a nova posição com a rotação
            nova_posicao = (ord(char.lower()) - ord('a') + rotacoes) % 26
            # Substitui a letra original pela nova letra rotacionada
            nova_letra = chr(ord('a') + nova_posicao)
            if is_upper:
                nova_letra = nova_letra.upper()
            texto_cifrado += nova_letra
        else:
            # Mantém caracteres que não estão no alfabeto (como pontuações e espaços)
            texto_cifrado += char
    
    return texto_cifrado

# Exemplo de uso
texto = "Ola, meu nome é Carlos! Seu?"
rotacoes = 7
print(rotacionar_texto(rotacoes, texto))  # Output: "Vsh, tlb uvtl é Jhysvz! Zlb?"
