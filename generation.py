import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
list_chars = []
flag = True

while flag:
    pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
    if pwd_quantity<1:
        print('Таково не может быть...')
    else:
        flag = False

flag = True

while flag:
    pwd_len = int(input('Какой длины должен быть пароль? '))
    if pwd_len<8:
        print('Безопасным пароль может быть только от 8 символов')
    else:
        flag = False

pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')

if pwd_digits.lower() == 'Да' or pwd_digits.lower() == 'да' or pwd_digits.lower() == 'д' or pwd_digits.lower() == '1':
    chars += digits
if pwd_lowercase.lower() == 'Да' or pwd_lowercase.lower() == 'да' or pwd_lowercase.lower() == 'д' or pwd_lowercase.lower() == '1':
    chars += lowercase_letters
if pwd_uppercase.lower() == 'Да' or pwd_uppercase.lower() == 'да' or pwd_uppercase.lower() == 'д' or pwd_uppercase.lower() == '1':
    chars += uppercase_letters
if pwd_punctuation.lower() == 'Да' or pwd_punctuation.lower() == 'да' or pwd_punctuation.lower() == 'д' or pwd_punctuation.lower() == '1':
    chars += punctuation
if pwd_exceptions.lower() == 'Да' or pwd_exceptions.lower() == 'да' or pwd_exceptions.lower() == 'д' or pwd_exceptions.lower() == '1':
    for c in 'il1Lo0O':
        chars.replace(c,'')

def generate_password(length, chars):
    random.shuffle(list(chars))
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

for i in range(pwd_quantity):
    print(generate_password(pwd_len, chars))