# крестики-нолики
field = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]
count = 0

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+' '+' '.join(field[i]))
show_field(field)

def user_input(field):
    while True:
        place = input('Введите координаты: ').split()

        if len(place) !=2:
            print('Введите 2 координаты')
            continue

        x, y = place

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа')
            continue

        x, y = int(x), int(y)
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print('Вы вышли из диапазона')
            continue

        if field[x][y] != '-':
            print('Клетка занята')
            continue
        return x, y
user_input(field)

count = 0
def win(field, user):
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cords:
        symbols= []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

while True:
    count += 1
    if count % 2 == 1:
        user = 'X'
    else:
        user = 'O'
    x, y = user_input(field)
    field[x][y] = user
    show_field(field)
    if count == 9:
        print('Ничья')
        break
    if win(field,user):
        print(f"Выиграл {user}")
        break
count += 1



