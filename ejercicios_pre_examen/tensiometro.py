file = open('tensiometro.txt')
lines = file.readlines()

num_max = 250
num_min = 0

for i in range(1, len(lines)):
    element = lines[i].split(' ')
    if int(element[2]) > int(element[0]):
        print('MAL')
    elif int(element[0]) > num_max or int(element[2]) > num_max:
        print('MAL')
    elif int(element[0]) < num_min or int(element[2]) < num_min:
        print('MAL')
    else:
        print('BIEN')

