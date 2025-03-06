def justify(words, width): # função para justificar

    '''o while a seguir separa as palavras em listas que representam as linhas do texto justificado, a separação é
    feita de modo que, em cada linha, a soma do comprimento das palavras e dos espaços mínimos não seja superior ao
    comprimento exigido'''
    text = []
    while words: 
        line = []
        line_w = 0
        for i in words:
            if len(i) > width:
                raise ValueError(f'String "{i}" is greater than width')
            elif line_w + len(i) + words.index(i) > width:
                break
            else:
                line_w += len(i)
                line.append(i)

        for i in line:
            words.remove(i)

        text.append(line)

    '''o seguinte bloco de código concatena cada linha, adicionando os espaços sobrando'''
    result = []
    for line in text:
        spaces = width - sum([len(i) for i in line])
        if len(line) == 1:
            result.append(line[0] + ' ' * spaces)
        else:
            line_aux = ''
            spaces_r = spaces % len(line)
            for word in line:
                if spaces_r == 0:
                    line_aux += word + (' ' * (spaces // len(line)))
                else:
                    line_aux += word + (' ' * (spaces // len(line) + 1))
                    spaces_r -= 1
            result.append(line_aux)

    return result # retorna o texto formatado em forma de uma lista das linhas



num, width = map(int,input().split()) # recebe o N número de palavras e a largura das linhas
words = [input() for _ in range(num)] # recebe as N palavras

text = justify(words, width) # recebe uma lista das linhas justificadas
for _ in text:
    print(_)