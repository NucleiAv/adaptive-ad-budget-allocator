import sqlite3

def balance_algorithm(query_stream):
    conn = sqlite3.connect('advertisers.db')
    cursor = conn.cursor()

    # Load all advertisers into memory once
    cursor.execute("SELECT advertiser, bids, budget FROM advertisers_copy")  # Using the correct column name
    advertisers_data = cursor.fetchall()

    # Initialize dictionaries for fast access
    advertisers = {}
    for adv in advertisers_data:
        advertisers[adv[0]] = {
            'bids': adv[1].split(','),  # Split bids into a list
            'budget': adv[2]
        }

    transactions = []
    serial_no = 1

    # Process each character in the query stream
    for char in query_stream:
        # Find eligible advertisers in a single pass
        eligible_advertisers = [
            adv_name for adv_name, data in advertisers.items()
            if char in data['bids'] and data['budget'] > 0
        ]

        if eligible_advertisers:
            # Select the advertiser with the highest remaining budget
            winner = max(eligible_advertisers, key=lambda x: advertisers[x]['budget'])

            # Update the winner's budget
            advertisers[winner]['budget'] -= 1

            # Record the transaction
            transactions.append((serial_no, winner))
            serial_no += 1

    # Update the database in one go after processing the stream
    for adv_name, data in advertisers.items():
        cursor.execute("UPDATE advertisers_copy SET budget = ? WHERE advertiser = ?", (data['budget'], adv_name))

    # Commit the updates once after all processing
    conn.commit()
    conn.close()

    return transactions


# Read query stream from file
with open('query_stream.txt', 'r') as f:
    query_stream = f.read()

# Run the balance algorithm
transactions = balance_algorithm(query_stream)

# Save the transactions to a file
with open('transactions_basic.txt', 'w') as f:
    for transaction in transactions:
        f.write(f"{transaction[0]},{transaction[1]}\n")
