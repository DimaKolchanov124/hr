if "'Условие'":
    ()
# Начало блока кода.
# Выполнится, если условие True.
# Один отступ вправо от уровня объявления условного оператора
# Конец блока кода
else:
    ()
# Начало блока кода.
# Выполнится, если условие False.
# Один отступ вправо от уровня объявления условного оператора
...
# Конец блока кода
# Код который будет выполняться
#после условного оператора. Один отступ влево, чтобы закончить объявление цикла

#беру зонт, надеть сапоги, иду гулять
is_raininy = True #будет  дождь
if is_raininy:
    print('беру зонт')
    print('надеть ссапоги')
else:
    print('не беру зонт')
print('иду гулять')

# не беру зонт, иду гулять
is_raininy = False #дождя не будет
if is_raininy:
    print('беру зонт')
    print('надеть ссапоги')
else:
    print('не беру зонт')
print('иду гулять')

#беру зонт, иду гулять
is_raininy = True #будет  дождь
if is_raininy:
    print('беру зонт')
print('иду гулять')

#иду гулять
is_raininy = False #дождя не будет
if is_raininy:
    print('беру зонт')
print('иду гулять')

#беру дождевик, иду гулять
is_raininy = True #будет  дождь
heavy_rain = False
if is_raininy:
    if heavy_rain:
        print('беру зонт')
    else:
        print('беру  дождевик')
else:
    print('не беру зонт')
print('иду гулять')


#беру зонт, иду гулять
is_raininy = True #будет  дождь
heavy_rain = True
if is_raininy:
    if heavy_rain:
        print('беру зонт')
    else:
        print('беру  дождевик')
else:
    print('не беру зонт')
print('иду гулять')

print('gznm ,jkmit  nh`[', 5 > 3)
print('lkbyyf ckjjdf hfdyf 1?', len("hello") == 1)
print('7 yt hfdyj 12?', 7 != 12)

