import modul
import logger

print('Добро пожаловать в телефонный справочник!')
print('Для выбора режима нажмите:')
print('\n Добавление данных - <1>\n Поиск абонента - <2>\n Вывод справочника - <3>')
print('')
a = int(input ('=> '))
if int(a) == 1:
    logger.record_telephone_directory(modul.adding_data())
elif a == 2:
    print(modul.search_subscriber(logger.reading_telephone_directory()))
elif a == 3:
    print(logger.reading_telephone_directory())
else:
    print('Режим в разработке')
