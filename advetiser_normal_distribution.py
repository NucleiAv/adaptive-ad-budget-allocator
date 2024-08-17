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

# Pre-calculate keyword frequencies for assertions
keyword_frequencies = {kw: count / total_budget for kw, count in keyword_counts.items()}

# Initial budget allocation using normal distribution
mean_budget = total_budget / num_advertisers
std_dev = mean_budget / 4  # Adjust for desired distribution spread

advertiser_budgets = {}
for i in range(num_advertisers):
    advertiser = f'A{i+1}'
    budget = max(1, int(random.normalvariate(mean_budget, std_dev)))  # Ensure at least 1
    advertiser_budgets[advertiser] = budget
    total_budget -= budget

# Redistribute remaining budget using normal distribution (in a loop)
while total_budget > 0:
    for advertiser in advertiser_budgets.keys():
        redistribution = max(1, int(random.normalvariate(0, std_dev / 2)))  # Smaller adjustments
        if redistribution > total_budget:
            redistribution = total_budget  # Ensure not overspending
        advertiser_budgets[advertiser] += redistribution
        total_budget -= redistribution

# Keyword selection and assertion
all_keywords = list(keyword_counts.keys())
for advertiser, budget in advertiser_budgets.items():
    keywords = random.sample(all_keywords, random.randint(1, 10))

    # Assertion check: Ensure each advertiser's budget doesn't exceed keyword costs
    allocated_cost = sum(keyword_frequencies[keyword] * total_budget for keyword in keywords)
    assert allocated_cost <= budget, f"Budget for {advertiser} exceeds expected keyword costs!"

    cursor.execute('''INSERT INTO advertisers VALUES (?, ?, ?)''', (advertiser, ','.join(keywords), budget))

# Duplicate the advertisers table
cursor.execute("CREATE TABLE advertisers_copy AS SELECT * FROM advertisers")
conn.commit()
conn.close()
