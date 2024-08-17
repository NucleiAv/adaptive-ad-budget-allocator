import sqlite3

with open('transactions_basic.txt', 'r') as f:
    transactions = [line.strip().split(',') for line in f]

total_revenue = len(set(int(serial_no) for serial_no, _ in transactions))

spending_per_advertiser = {}
for _, advertiser in transactions:
    spending_per_advertiser[advertiser] = spending_per_advertiser.get(advertiser, 0) + 1

with open('results_basic.txt', 'w') as f:
    f.write(f"Total Revenue: {total_revenue}\n")
    for advertiser, spending in spending_per_advertiser.items():
        f.write(f"{advertiser}: {spending}\n")
