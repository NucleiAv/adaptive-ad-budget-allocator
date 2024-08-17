import random
import string

length =  100000
num_keywords = 20 # Adjust this based on your desired number of keywords

# Create a list of keywords (you can customize this)
keywords = random.sample(string.ascii_lowercase, num_keywords) 

# Generate the query stream with more repetition and better distribution
query_stream = []
for _ in range(length):
    query_stream.append(random.choices(keywords, k=1)[0])  # Choose a keyword randomly, with higher chances for repetition
query_stream = "".join(query_stream)

with open('query_stream.txt', 'w') as f:
    f.write(query_stream)
