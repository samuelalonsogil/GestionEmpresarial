file = open('nums..txt')
lines = file.readlines()

for i in range(1, len(lines)):
    line = lines[i]
    a = int(line.split(' ')[0])
    b = int(line.split(' ')[1])
    c = int(line.split(' ')[2])
    d = int(line.split(' ')[3])
    bajado = b * c - d
    subido = bajado + a * b
    print(str(bajado), str(subido))
