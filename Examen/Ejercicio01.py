file = open('datos.txt')
lines = file.readlines()

for i in range(1, len(lines) - 1):
    aux = 1
    num = 0
    for n in range(len(lines[i])):
        num += int(lines[i]) % aux
        aux *= 10
    print(num)



