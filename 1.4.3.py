'''3. Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну.
Виконав: Лещенко В. О.

В даному випадку доцільно використовувати рекурсію.
Час розробки рекурсії менший, затрачений час на виконання програми практично однаковий як і з рекурсією, так і з ітераціями.
Читабельність краща у випадку з рекурсією.'''

import timeit

def dec_to_hex_rec(n): # рекурсія
    n, remainder = n // 16, hex_number[n % 16] # ділимо число націло на 16 і знаходимо остачу від ділення
    if n:
        return dec_to_hex_rec(n) + remainder # якщо поділилось, то додаємо до результата остачу і виводимо
    return remainder # інакше - просто виводимо остачу

def dec_to_hex_iter(n): # ітерація
    hex_str = '' # пустий рядок
    if n == 0: # нуль в десятковій = нуль в 16-ній
        return 0
    while n != 0: # поки не дорівнює нулю, буде відбуватись конкатенація рядків остач
        hex_str += hex_number[n % 16]
        n = n // 16
    return hex_str[::-1] # виводимо в оберненій формі

hex_number = "0123456789ABCDEF" # змінна, де зберігаються числа і букви в 16-ній системі
n = int(input('Введіть число n: '))
question = int(input('Який спосіб використовувати: рекурсія (1) чи ітерація (2): '))
if question == 1:
    print(f'Число {n} у 16-річній системі числення: {dec_to_hex_rec(n)}')
elif question == 2:
    print(f'Число {n} у 16-річній системі числення: {dec_to_hex_iter(n)}')
print('Затрачений час: ', timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))