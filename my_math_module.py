# напишем модуль
def my_add(x,y):
    return x+y
def my_sub(x,y):
    return x-y
def my_mul(x,y):
    return x*y
def my_div(x,y):
    return x/y

# Числа Фибоначчи
# 1, 1, 2, 3, 5, 8, 13, 21 ...
# напишем вычисление с помощью рекурсивных функций
def fib_num(n):
    if n==1: return 1
    elif n==2: return 1
    else: return fib_num(n-1) + fib_num(n-2)
#print(fib_num(7))

# перепишем эту функцию с помощью lambda функции:
fib_num_l = lambda n: fib_num_l(n-1) + fib_num_l(n-2) if n>2 else 1 # на вход параметр n, вызываем её же (fib_num_l), но с параметрами (n-1) и (n-2), если n>2. Иначе 1.
#print(fib_num_l(7))

# МЫ СОЗДАЛИ МОДУЛЬ. ТЕПЕРЬ СОЗДАДИМ ЕЩЕ ОДИН ФАЙЛ MAIN

if __name__ == '__main__':
    n = 10
    if fib_num_l(n)**2 + fib_num_l(n+1)**2 == fib_num_l(2*n+1):
        print('Свойство работает')
    else: print('Свойство не работает')
# если мы сейчас вызовем модуль my_math_module из-под файла main, то все результаты работы модуля my_math_module появятся в результатах работы файла main
# чтобы этого не было, см. строку 26