n = input('введіть 5 значне число: ')
n = int(n)
print( 'число перевернуте:', end='')
print(n % 10, end='')
print(n % 100 // 10, end='')
print(n % 1000 // 100, end='')
print(n % 10000 // 1000, end='')
print(n // 10000)