import sqlite3
import random
import numpy as np
from collections import Counter  # Import Counter from collections

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

# Generate budgets with extreme values and missing values
advertiser_budgets = {}
for i in range(num_advertisers):
    advertiser = f'A{i+1}'

    # Randomly choose between different normal distributions to create outliers
    distribution_choice = random.random()
    if distribution_choice < 0.3:  # 30% chance of low-budget outlier
        budget = max(1, int(np.random.normal(loc=50, scale=10)))
    elif distribution_choice < 0.6:  # 30% chance of mid-budget (closer to average)
        budget = max(1, int(np.random.normal(loc=total_budget // num_advertisers, scale=50)))
    else:  # 40% chance of high-budget outlier
        budget = max(1, int(np.random.normal(loc=2000, scale=300)))

    # Introduce missing values (e.g., 10% chance of no budget)
    if random.random() < 0.1:
        budget = 0

    advertiser_budgets[advertiser] = budget

# Adjust total budget and insert into database
allocated_budget = sum(advertiser_budgets.values())
if allocated_budget != total_budget:
    # Simple adjustment: deduct excess from the highest budget advertiser
    highest_budget_advertiser = max(advertiser_budgets, key=advertiser_budgets.get)
    advertiser_budgets[highest_budget_advertiser] -= (allocated_budget - total_budget)

for advertiser, budget in advertiser_budgets.items():
    keywords = random.sample(available_keywords, random.randint(1, 10))
    cursor.execute('''INSERT INTO advertisers VALUES (?, ?, ?)''', (advertiser, ','.join(keywords), budget))

# Duplicate the advertisers table
cursor.execute("CREATE TABLE advertisers_copy AS SELECT * FROM advertisers")
conn.commit()
conn.close()
