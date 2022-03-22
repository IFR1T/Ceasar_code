def is_valid_number(text):
    if text.isdigit():
        return True
    return False

def ceasar_coder(language, decoder, key, text):
    text_list = list(text)
    if language == 'en':
        abc = 26
        start1, start2 = ord('A'), ord('a')
        end1, end2 = ord('Z'), ord('z')
    else:
        abc = 32
        start1, start2 = ord('А'), ord('а')
        end1, end2 = ord('Я'), ord('я')
    if decoder == 'ш':
        coder_symbol = 1
    else:
        coder_symbol = -1
    for i in range(len(text_list)):
        if start1 <= ord(text_list[i]) <= end1:
            text_list[i] = chr(((ord(text_list[i]) - start1) + (coder_symbol * key)) % abc + start1)
        if start2 <= ord(text_list[i]) <= end2:
            text_list[i] = chr(((ord(text_list[i]) - start2) + (coder_symbol * key)) % abc + start2)
    return ''.join(text_list)

print("Добро пожаловать к Цезарю, в его шифровальный алгоритм!")
while True:
    language = input('С каким языком будем работать? en - английский, все остальное - русский. \n')
    decoder = input('Будем зашифровывать или дешифровывать? ш - шифровка, все остальное - дешифровка. \n')
    while True:
        key = input('Какой у нас шаг шифровки? Введи любое число, или !, если хочешь сделать цикл проверки на все варианты. \n')
        if is_valid_number(key):
            key = int(key)
            break
        elif key == '!':
            if language == 'en':
                limit = 26
            else:
                limit = 32
            break
        else:
            print('Так мы ничего не добьемся, нужно ввести число.')
    text = input("Итак, какой у нас текст? \n")
    print('Чтож, а вот и результат:')
text = input().split()
for word in text:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    print(ceasar_coder('en', 'ш', count, word), end=" ")

#    if key != '!':
#        print(ceasar_coder(language, decoder, key, text))
#    else:
#        for i in range(1, limit):
#            print(ceasar_coder(language, decoder, i, text))
#    if input('Еще нужно что-то сделать? д - да, все остальное - нет. \n') != "д":
#        print("Чтож, удачи! Надеюсь, я был тебе полезен.")
#        break

