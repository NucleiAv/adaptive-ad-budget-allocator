import sqlite3

def balance_algorithm(query_stream):  # Removed window_size parameter
    conn = sqlite3.connect('advertisers.db')
    cursor = conn.cursor()

    transactions = []
    serial_no = 1

    for char in query_stream:  # Directly iterate over each character
        cursor.execute("SELECT * FROM advertisers")
        advertisers = cursor.fetchall()
        eligible_advertisers = [adv for adv in advertisers if char in adv[1].split(',') and adv[2] > 0 and adv[2] > adv[2] // 2]

        if eligible_advertisers:
            winner = max(eligible_advertisers, key=lambda x: x[2])  # Prioritize by highest remaining budget
            if winner[2] > 0:
                transactions.append((serial_no, winner[0]))
                serial_no += 1
                cursor.execute("UPDATE advertisers SET budget = budget - 1 WHERE advertiser = ?", (winner[0],))
                conn.commit()

    conn.close()
    return transactions


with open('query_stream.txt', 'r') as f:
    query_stream = f.read()

transactions = balance_algorithm(query_stream)

with open('transactions.txt', 'w') as f:
    for transaction in transactions:
        f.write(f"{transaction[0]},{transaction[1]}\n")
