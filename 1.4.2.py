'''2. Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе).
Виконав: Лещенко В. О.

Час розробки ітерації менший, затрачений час на виконання менший у випадку з рекурсією.
Читабельність краща у випадку з ітерацією.'''

import timeit

def prime_rec(n, i=2): # рекурсії, і - це дільник, починаємо із 2-ки
    if (n <= 2): # якщо число менше-рівне за 2
        if n == 2: # і дорінює 2 - то воно просте
            return True
        else:
            return False # інакше - не просте
    if (n % i == 0): # ящо воно націло ділиться на дільник, відмінний від 1 і самого себе - воно не просте
        return False
    if (i * i > n): # якщо не зустріли дільника числа до і, та якщо і^2 більше за це число, то число просте
        return True
    return prime_rec(n, i + 1) # знову застосовуємо функцію, збільшуєчи дільник на 1

def prime_iter(n): # ітерація
    if n > 1: # дільник має бути більше 1
        for i in range(2, n): # ідемо за допомогою діапазону від 2 до самого числа
            if (n % i) == 0: # якщо ділиться на дільник націло - то число не є простим
                return False
        else:
            return True # інакше - просте
    else:
        return False # якщо дільник рівний або менший за 1, то число не є простим

n = int(input('Введіть число n: '))
question = int(input('Який спосіб використовувати: рекурсія (1) чи ітерація (2): '))
if question == 1:
    if prime_rec(n): # якщо true - число просте
        print(f'Число {n} просте.')
    else: # false - не просте
        print(f'Число {n} не є простим.')
if question == 2:
    if prime_iter(n):
        print(f'Число {n} просте.')
    else:
        print(f'Число {n} не є простим.')
print('Затрачений час: ', timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))