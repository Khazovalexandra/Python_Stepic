import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут? ')
print('Привет, '+ name)
flag = True
while flag:
    print('На какой вопрос ты хочешь услышать ответ?')
    str = input()
    print('Мой ответ: '+random.choice(answers))
    print('Еще вопрос?')
    next = input('Если да жми - Да/д/1 ')
    if next == 'Да' or next == 'да' or next == 'д' or next == '1':
        flag = True
    else:
        flag = False

print('Возвращайся если возникнут вопросы!')