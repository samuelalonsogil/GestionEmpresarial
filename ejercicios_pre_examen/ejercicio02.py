
file = open('nums..txt')
lines = file.readlines()

for i in range(1, len(lines)):
    line = lines[i]
    neto = int(line.split(' ')[0])
    total = int(line.split(' ')[1])
    diferencia = total-neto
    print(str(diferencia))
