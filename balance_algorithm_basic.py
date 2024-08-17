import sqlite3

def balance_algorithm(query_stream):
    conn = sqlite3.connect('advertisers.db')
    cursor = conn.cursor()

    transactions = []
    serial_no = 1

    for char in query_stream:
        cursor.execute("SELECT * FROM advertisers_copy")  
        advertisers = cursor.fetchall()
        eligible_advertisers = [adv for adv in advertisers if char in adv[1].split(',') and adv[2] > 0]

        if eligible_advertisers:
            winner = min(eligible_advertisers, key=lambda x: x[2])  # Prioritize by lowest remaining budget
            transactions.append((serial_no, winner[0]))
            serial_no += 1

            cursor.execute("UPDATE advertisers_copy SET budget = budget - 1 WHERE advertiser = ?", (winner[0],))
            conn.commit()

    conn.close()
    return transactions

with open('query_stream.txt', 'r') as f:
    query_stream = f.read()

transactions = balance_algorithm(query_stream)

with open('transactions_basic.txt', 'w') as f:
    for transaction in transactions:
        f.write(f"{transaction[0]},{transaction[1]}\n")
