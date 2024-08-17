import sqlite3

def balance_algorithm(query_stream, window_size=100):
    conn = sqlite3.connect('advertisers.db')
    cursor = conn.cursor()

    transactions = []
    serial_no = 1

    for i in range(0, len(query_stream), window_size):
        window = query_stream[i:i + window_size]

        for char in window:
            cursor.execute("SELECT * FROM advertisers")
            advertisers = cursor.fetchall()
            eligible_advertisers = [adv for adv in advertisers if char in adv[1].split(',') and adv[2] > 0 and adv[2] > adv[2] // 2]

            if eligible_advertisers:
                winner = max(eligible_advertisers, key=lambda x: x[2]) # Prioritize by highest remaining budget
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
