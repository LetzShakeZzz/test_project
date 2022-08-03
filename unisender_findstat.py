def get_params(file):
    params = file.readline().split(';')
    return params

with open('stats.csv', encoding='utf-8') as file:
    enquiery = input('Введите адрес ящика:')
    params = get_params(file)
    for line in file.readlines():
        data = line.split(';')
        if data[0] == enquiery:
            result = {key: value for key, value in zip(params, data)}
            for key, value in result.items():
                print(f'{key}: {value}')