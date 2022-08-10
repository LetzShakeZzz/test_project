from datetime import datetime, timedelta

def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f'{amount} {declensions[0]}'
    elif 2 <= amount % 10 <= 4 and amount % 100 not in (12, 13, 14):
        return f'{amount} {declensions[1]}'
    return f'{amount} {declensions[2]}'

day = ("день", "дня", "дней")
hour = ("час", "часа", "часов")
minute = ("минута", "минуты", "минут")
release_date = datetime(2022, 11, 8, 12, 0)
current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
remaining_time = release_date - current_date

if release_date > current_date:
    if remaining_time.days and remaining_time.seconds // 3600:
        print(f'До выхода курса осталось: {choose_plural(remaining_time.days, day)} и {choose_plural(remaining_time.seconds // 3600, hour)}')
    elif remaining_time.days and not remaining_time.seconds // 3600:
        print(f'До выхода курса осталось: {choose_plural(remaining_time.days, day)}')
    elif not remaining_time.days and remaining_time.seconds // 3600 and (remaining_time.seconds // 60) % 60:
        print(f'До выхода курса осталось: {choose_plural(remaining_time.seconds // 3600, hour)} и {choose_plural((remaining_time.seconds // 60) % 60, minute)}')
    elif not remaining_time.days and remaining_time.seconds // 3600 and not (remaining_time.seconds // 60) % 60:
        print(f'До выхода курса осталось: {choose_plural(remaining_time.seconds // 3600, hour)}')
    elif not (remaining_time.days and remaining_time.seconds // 3600) and (remaining_time.seconds // 60) % 60:
        print(f'До выхода курса осталось: {choose_plural((remaining_time.seconds // 60) % 60, minute)}')
else:
    print('Курс уже вышел!')