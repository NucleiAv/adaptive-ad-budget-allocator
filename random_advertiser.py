import sqlite3
import random
from collections import Counter

conn = sqlite3.connect('advertisers.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS advertisers 
                  (advertiser TEXT, bids TEXT, budget INTEGER)''')

with open('query_stream.txt', 'r') as f:
    query_stream = f.read()

keyword_counts = Counter(query_stream)
total_budget = len(query_stream)
num_advertisers = 25
available_keywords = list(keyword_counts.keys())

# Random budget allocation
advertiser_budgets = {}
for i in range(num_advertisers):
    advertiser = f'A{i+1}'
    advertiser_budgets[advertiser] = random.randint(1, total_budget) 

# Adjust budgets to match total budget
allocated_budget = sum(advertiser_budgets.values())
while allocated_budget != total_budget:
    for advertiser, budget in advertiser_budgets.items():
        if allocated_budget > total_budget:
            if budget > 1:  # Avoid reducing budget to zero
                advertiser_budgets[advertiser] -= 1
                allocated_budget -= 1
        elif allocated_budget < total_budget:
            advertiser_budgets[advertiser] += 1
            allocated_budget += 1

# Keyword selection and insertion
for advertiser, budget in advertiser_budgets.items():
    keywords = random.sample(available_keywords, random.randint(1, 10))  # Select random keywords
    cursor.execute('''INSERT INTO advertisers VALUES (?, ?, ?)''', (advertiser, ','.join(keywords), budget))

# Duplicate the advertisers table
cursor.execute("CREATE TABLE advertisers_copy AS SELECT * FROM advertisers")
conn.commit()
conn.close()
