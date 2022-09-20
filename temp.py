import csv, json

with open('prices.json', encoding='UTF-8') as prices_file:

    prices = json.load(prices_file)
    total_sales = 0

    for i in range(1, 5):
        with open(f'quarter{i}.csv', encoding='UTF-8') as season_file:
            _, *csv_data = csv.reader(season_file)
            for entry in csv_data:
                product, *quantity = entry
                total_sales += sum(map(int, quantity)) * prices[product]

    print(total_sales)

