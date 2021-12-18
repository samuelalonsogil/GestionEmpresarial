f = open('mensajes', 'r')
lineas = f.readlines()
for linea in lineas:
    i = 0
    frase = ''

    while i < len(linea) - 1:
        n = int(linea[i] + linea[i + 1])
        if n < 32:
            i += 3
        else:
            i += 2
        l = chr(n)
        frase = frase + l
    print(frase)
