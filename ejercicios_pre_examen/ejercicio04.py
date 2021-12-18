file = open('entradas.txt')
lines = file.readlines()

for i in range(1, len(lines)):
    t = lines[i].split(' ')
    ceros = False
    nueves = False
    for n in t:
        n = float(n)
        if n == 0:
            ceros = True
        if n >= 9:
            nueves = True
            break
    if not nueves and ceros:
        print('suspenso directo')
    else:
        print('media')
