import random

print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if n.isdigit() and 1<=int(n)<=d:
        return True
    else:
        print(f'А может быть все-таки введем целое число от 1 до {d}?')
        return False

play = True
while play:
    count = 1
    flag = True
    print('Введите диапозон для генерации числа')
    d = int(input())
    r = random.randint(1, d)

    while flag:
        print('Введите число')
        num = input()
        if is_valid(num):
            num = int(num)
        else:
            continue
        if num < r:
            count+=1
            print('Ваше число МЕНЬШЕ загаданного, попробуйте еще разок')
        elif num > r:
            count+=1
            print('Ваше число БОЛЬШЕ загаданного, попробуйте еще разок')
        elif num == r:
            print('Вы угадали, поздравляем!')
            print(f'Для этого вам понадобилось {count} попыток')
            flag = False
        
    print('Сыграем еще? Если да, то вводи: Да/д/1')
    str = input()
    if str == 'д' or str == 'Да' or str == 'да' or str == '1':
        play = True
    else:
        play = False
    
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')