from datetime import datetime, timedelta, date

try:
    print('Введите дату рождения в формате ДД/ММ/ГГ')
    birthday = datetime.strptime(input(), "%d/%m/%y")
except ValueError:
    print('Дата в неверном формате')
    exit()
time_1 = timedelta(days=10000)
time_2 = timedelta(minutes=1000000)
time_3 = timedelta(seconds=1000000000)
print(datetime.date(birthday + time_1))
print(datetime.date(birthday + time_2))
print(datetime.date(birthday + time_3))
