upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def user_choices():
    while True:    # определение direction
        global direction
        direction = int(input('Нужна шифровка(1) иди дешифровка(2)? Введите: 1/2'))
        if direction in [1, 2]:
            break
        else:
            print('Не удалось опознать ввод. Пожалуйста, введите: 1/2 для шифровки(1) иди дешифровки(2)')
            continue

    while True:    # определение language
        global language
        language = input('Введите желаемый язык: ru/en').lower().strip()
        if language in ['ru', 'en']:
            break
        else:
            print('Не удалось опознать ввод. Пожалуйста, введите: en/ru')
            continue

    global shift
    shift = int(input('Введите шаг сдвига'))    # определение shift

    global s
    s = input('Введите сообщение').strip()    # строка текста для шифровки/дешифровки

    return direction, language, shift, s


def decoding(direction, language, shift, s):
    if language == 'en':
        if direction == 1:
            for c in s:
                if c in lower_eng_alphabet:
                    if ord(c) + shift > 122:
                        print(chr(ord(c) + shift - 26), end='')
                    else:
                        print(chr(ord(c) + shift), end='')
                elif c in upper_eng_alphabet:
                    if ord(c) + shift > 90:
                        print(chr(ord(c) + shift - 26), end='')
                    else:
                        print(chr(ord(c) + shift), end='')
                else:
                    print(c, end='')
        elif direction == 2:
            for c in s:
                if c in lower_eng_alphabet:
                    if ord(c) - shift < 97:
                        print(chr(ord(c) - shift + 26), end='')
                    else:
                        print(chr(ord(c) - shift), end='')
                elif c in upper_eng_alphabet:
                    if ord(c) - shift < 65:
                        print(chr(ord(c) - shift + 26), end='')
                    else:
                        print(chr(ord(c) - shift), end='')
                else:
                    print(c, end='')
    elif language == 'ru':
        if direction == 1:
            for c in s:
                if c in lower_rus_alphabet:
                    if lower_rus_alphabet.index(c) + shift < 32:
                        print(lower_rus_alphabet[lower_rus_alphabet.index(c) + shift], end='')
                    else:
                        print(lower_rus_alphabet[shift - (32 - lower_rus_alphabet.index(c))], end='')
                elif c in upper_rus_alphabet:
                    if upper_rus_alphabet.index(c) + shift < 32:
                        print(upper_rus_alphabet[upper_rus_alphabet.index(c) + shift], end='')
                    else:
                        print(upper_rus_alphabet[shift - (32 - upper_rus_alphabet.index(c))], end='')
                else:
                    print(c, end='')
        elif direction == 2:
            for c in s:
                if c in lower_rus_alphabet:
                    if lower_rus_alphabet.index(c) - shift >= 0:
                        print(lower_rus_alphabet[lower_rus_alphabet.index(c) - shift], end='')
                    else:
                        print(lower_rus_alphabet[32 - (shift - lower_rus_alphabet.index(c))], end='')
                elif c in upper_rus_alphabet:
                    if upper_rus_alphabet.index(c) - shift >= 0:
                        print(upper_rus_alphabet[upper_rus_alphabet.index(c) - shift], end='')
                    else:
                        print(upper_rus_alphabet[32 - (shift - upper_rus_alphabet.index(c))], end='')
                else:
                    print(c, end='')


def starting_program():
    user_choices()
    decoding(direction, language, shift, s)
    print('\n')


while True:
    starting_program()
    if input('Нужна ли еще помощь? Введите: "да" или любой другой ввод для выхода из программы') == 'да':
        continue
    else:
        break
