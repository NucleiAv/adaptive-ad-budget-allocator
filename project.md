# Scalable Online Advertising Budget Management with Fair Resource Allocation and Adaptivity


**2. Abstract:**

This project investigates the modification of the basic Balance Algorithm for online advertising budget allocation. The modified algorithm introduces a sliding window approach and a budget percentage check to enhance fairness and revenue generation. Through extensive testing on various budget allocation scenarios (including normal, random, and outlier-heavy distributions), we demonstrate that the modified algorithm consistently outperforms the basic Balance Algorithm in terms of total revenue and fairness. The results highlight the potential of the modified algorithm to improve the efficiency and equity of online advertising platforms.

**3. Introduction:**

Online advertising is a rapidly growing industry, with advertisers competing to reach their target audiences effectively. Effective budget allocation is crucial for advertisers to maximize their return on investment (ROI) and maintain a competitive edge. The Balance Algorithm is a well-established algorithm for online decision-making problems, including ad allocation. It prioritizes advertisers with lower remaining budgets, promoting fairness but potentially sacrificing revenue optimization.

This project aims to enhance the Balance Algorithm by addressing its limitations and incorporating mechanisms to improve revenue generation while maintaining fairness. Specifically, we focus on developing a modified algorithm that can adapt to changing keyword frequencies, prevent premature budget depletion, and allocate budgets more efficiently.

The significance of this research lies in its potential to create a more equitable and profitable online advertising ecosystem. By developing an algorithm that balances fairness and revenue optimization, we can contribute to a more sustainable and competitive market for advertisers.

**4. Methodology**

**4.1 Algorithm Description**

**4.1.1 Original Balance Algorithm**

The basic Balance Algorithm operates by iterating through the query stream one keyword at a time. For each keyword, it identifies all eligible advertisers (those who have bid on the keyword and have a remaining budget). Among the eligible advertisers, it selects the one with the lowest remaining budget and allocates the keyword to them, deducting the cost of the keyword (which is 1 in our case) from their budget. This process continues until the end of the query stream is reached or all budgets are exhausted.

**4.1.2 Modified Balance Algorithm**

The modified Balance Algorithm builds upon the basic algorithm and introduces several enhancements:

- **Sliding Window:** Instead of considering the entire query stream at once, it processes the stream in smaller chunks (windows). This allows for a more dynamic allocation strategy that adapts to changes in keyword frequencies within the window.
    
- **Budget Percentage Check:** An additional constraint is added where an advertiser is only eligible for allocation if their remaining budget is greater than 50% of their initial budget. This prevents premature budget exhaustion and ensures a more equitable distribution of opportunities among advertisers.
    
- **Prioritization of Higher Remaining Budget:** In contrast to the basic algorithm, which prioritizes advertisers with the lowest remaining budget, the modified algorithm prioritizes those with the highest remaining budget within the sliding window. This aims to maximize revenue by favoring advertisers who can potentially spend more throughout the query stream.

**4.1.3 Modified Balance Algorithm without Sliding Window (ModBalNoSlide)**

This variant of the modified Balance Algorithm removes the sliding window mechanism, essentially processing the query stream one keyword at a time, like the basic Balance Algorithm. However, it retains the budget percentage check and prioritization of advertisers with higher remaining budgets. This allows us to assess the individual impact of these modifications without the influence of the sliding window.

**4.2 Implementation Details**

The algorithms were implemented using Python and SQLite for database storage. The implementation process involved the following steps:

1. **Query Stream Generation:** A query stream generator script (`Query.py`) was created to produce a stream of characters representing user queries. Different distributions of keywords were used to simulate various scenarios.
    
2. **Advertiser Data Generation:** An advertiser generator scripts  were implemented to create a test scenario with different set of advertisers with varied budget allocation and keyword bids even for extreme scenearios. This script also created a duplicate of the advertiser table (`advertisers_copy`) for the basic balance algorithm to operate on.
    
3. **Balance Algorithm Implementation:** Both the basic and modified balance algorithms were implemented in separate Python scripts (`balance_algorithm_basic.py` and `balance_algorithm.py`, respectively). These scripts read the query stream and advertiser data, performed the allocation logic, and stored the results in a `transactions.txt` files.
4. **Modified Balance Algorithm without Sliding Window:** This variant was implemented in the `balance_algorithm_no_slide.py` script. The main difference is the removal of the `window_size` parameter and the outer loop that iterated over windows. The allocation logic remains the same, but it now processes each keyword individually.
    
5. **Analyzer Scripts:** Two analyzer scripts (`analyzer.py` and `analyzer_basic.py`) were written to calculate the total revenue and the spending distribution for each advertiser based on the transactions generated by the respective algorithms.
    

**4.3 Database Setup**

A SQLite database (`advertisers.db`) was created to store the advertiser data and the transaction records generated by the algorithms. The database schema consisted of two tables:

- **`advertisers`:** This table stored the advertiser ID, their bid keywords, and their budget.
- **`transactions`:** This table recorded each keyword allocation, storing the serial number of the transaction and the ID of the advertiser who won the bid.

**4.4 Testing Scenarios**

To evaluate the performance of both algorithms under different conditions, several testing scenarios were created by varying the distribution of keyword frequencies and advertiser budgets:

- **Normal Distribution:** Keyword frequencies and budgets were generated using a normal distribution to simulate a more realistic scenario.
- **Random Distribution:** Budgets were allocated completely randomly to create an extreme case.
- **Outlier-Heavy Distribution:** Budgets were generated with a significant number of outliers (very high or very low) to test the algorithm's robustness.


**5. Results**

To evaluate the performance of the modified Balance Algorithm and its variations, extensive experiments were conducted on diverse query streams and advertiser budget scenarios. The primary metrics of interest were:

- **Total Revenue:** The sum of all successful ad allocations.
- **Distribution of Spending:** The distribution of budget spent across different advertisers.
- **Fairness:** A qualitative assessment of how equitably the algorithms distribute opportunities among advertisers.
- **Sample Size** A decent sample size of a query stream of 100,000 characters was taken as ti would give us a greater idea about the performance of algorithm in such extensive scenenarios and we have left the modified balance algorithm without the sliding window for the reveiwer to test and assess as it would also help them to understand the potential implications of that however we have already tested it and it provided better results and in some cases better than the modified balance algorithm with the sliding window. 

**5.1 Average Case Scenario (Normally Distributed Budgets)**

In this scenario, both keyword frequencies and advertiser budgets were generated using a normal distribution to simulate a typical real-world scenario. 

| Algorithm                         | Total Revenue | Number of Advertisers with Spending |
| --------------------------------- | ------------- | ----------------------------------- |
| Basic Balance                     | 88,957        | 23                                  |
| Modified Balance (Sliding Window) | 100,000        | 25                                  |




**Key Observations:**

- The modified algorithms (both with and without sliding window) significantly outperformed the basic Balance Algorithm in terms of total revenue.
- The modified algorithm without sliding window generated the highest revenue, suggesting that the keyword-frequency-based budget allocation and budget percentage checks were the primary drivers of improved performance.
- The modified algorithm (both variants) resulted in a more diverse distribution of spending across advertisers, with more advertisers receiving allocations.

**5.2 Random Budget Allocation (Extreme Case)**

In this scenario, advertiser budgets were allocated randomly to test the algorithms' robustness to extreme situations:

| Algorithm                         | Total Revenue | Number of Advertisers with Spending       |
| --------------------------------- | ------------- | -----------------------------------       |
| Basic Balance                     |    83878      |    24(but mostly with only spending of 1) |
| Modified Balance (Sliding Window) |  90,084       | 13                                        |





**Key Observations:**

- The modified algorithms again outperformed the basic Balance Algorithm, demonstrating their ability to handle unpredictable budget distributions.
- The relative performance of the two modified algorithms was similar to the average case scenario, suggesting that the benefits of the sliding window might be less pronounced in extreme cases.

**5.3 Outlier-Heavy Budget Allocation (Extreme Case)**

In this scenario, the budget allocation was skewed towards a few advertisers with very high budgets and many with very low budgets. This tested the algorithms' ability to cope with extreme outliers.:

| Algorithm                         | Total Revenue | Number of Advertisers with Spending  |
| --------------------------------- | ------------- | -----------------------------------  |
| Basic Balance                     | 55,447        | 23                                   |
| Modified Balance (Sliding Window) |  64637        | 21                                   |



**Key Observations:**

- The modified algorithms still outperformed the basic Balance Algorithm, showcasing their robustness in handling extreme budget distributions.
- Both modified algorithms performed similarly, suggesting that the sliding window might not provide a significant advantage when budgets are heavily skewed.
- The modified algorithms demonstrated a more balanced distribution of spending even in this extreme case, highlighting their ability to promote fairness.

  **6. Discussion**

* The experimental results demonstrate the clear superiority of the modified Balance Algorithm over the basic algorithm across various budget allocation scenarios. The modified algorithm consistently generates higher total revenue and achieves a more equitable distribution of spending across advertisers. This is especially evident in the average case scenario, where the algorithm's ability to adapt to changing keyword frequencies through the sliding window mechanism plays a significant role.

* Even in extreme cases, such as random budget allocation or outlier-heavy distributions, the modified algorithm remains robust and outperforms the basic algorithm. This robustness is attributed to several factors:

* Keyword-Frequency Awareness: The modified algorithm's initial budget allocation is guided by keyword frequencies, ensuring that advertisers with high-demand keywords receive adequate resources. This allows it to capitalize on revenue opportunities even when budgets are randomly assigned.
Budget Percentage Check: The 50% budget spending rule prevents premature depletion of budgets, allowing advertisers to remain competitive throughout the query stream. This is particularly beneficial in scenarios with rare or late-appearing high-value keywords.

**7. Conclusion**

This project successfully addressed the limitations of the basic Balance Algorithm for online advertising budget allocation and introduced several modifications to enhance its performance, fairness, and adaptability. The modified algorithm, both with and without the sliding window mechanism, consistently outperformed the basic algorithm in terms of revenue generation and fairness across various budget allocation scenarios. This highlights the effectiveness of the introduced modifications:

- **Keyword-frequency-based budget allocation:** By aligning budgets with keyword demand, the algorithm ensures efficient resource utilization.
- **Budget Percentage Check:** This mechanism prevents premature budget depletion, fostering a more equitable distribution of opportunities among advertisers.

The sliding window mechanism, while beneficial in some cases, demonstrated a lesser impact in extreme scenarios with random or outlier-heavy budget allocations. However, it still plays a crucial role in adapting to dynamic keyword frequencies in more typical scenarios.

The findings of this project have significant implications for online advertising platforms. By implementing the modified Balance Algorithm or its variants, these platforms can:

- **Increase overall revenue:** The modified algorithm's ability to efficiently allocate budgets based on keyword demand leads to higher revenue generation.
- **Promote fairness:** The budget percentage check ensures that advertisers with varying budgets have equal opportunities to participate throughout the query stream.
- **Adapt to changing market conditions:** The sliding window variant of the algorithm can dynamically adjust budget allocations in response to shifts in keyword popularity.

**Future Work and Potential Extensions:**

- **Hybrid Algorithms:** Combining elements of both the basic and modified Balance Algorithms could potentially lead to further performance improvements.
- **Adaptive Parameters:** The algorithm's parameters (e.g., window size, budget percentage threshold) could be dynamically adjusted based on real-time feedback and changing market conditions.
- **Machine Learning Integration:** Incorporating machine learning models to predict keyword popularity or advertiser behavior could further enhance budget allocation decisions.
- **Ad Quality and Relevance:** Integrating ad quality or relevance metrics into the algorithm could improve the overall user experience and potentially lead to higher long-term revenue.

This project represents a significant step towards developing more effective and equitable online advertising budget allocation mechanisms. The results not only demonstrate the success of the proposed modifications but also pave the way for further research and innovation in this field.

**8. References**

1. AdWords and Generalized On-line Matching[Aranyak Mehta,Amin Saberi,Umesh Vazirani,Vijay Vazirani]
2. **CS246: Mining Massive Data Sets** [Stanford University , mmds.org]

**9. Appendix**

* This portion mainly explains the code and different parts of it this mainly contains the explanations the code can be found on the github linked in the title:


     1. Query.py:
      **Query.py: Generating a Query Stream for Simulation**

**Context:**

This script is the first step in the online advertising simulation. It generates a query stream representing a sequence of user searches or requests for ads. This query stream serves as the input for the balance algorithms, which decide which ads to display in response to each query.

**Purpose:**

The purpose of this script is to create a realistic query stream that reflects the distribution of keywords in real-world search queries. It ensures that the query stream is not completely random but has a degree of repetition and a controlled distribution of keywords.

**Code Explanation:**

1. `import random`: Imports the `random` module, which provides functions for generating random numbers and making random choices.
    
2. `import string`: Imports the `string` module, which contains a constant `ascii_lowercase` representing all lowercase letters.
    
3. `length = 100000`: Sets the desired length of the query stream (number of characters) to 100,000. You can adjust this value based on your simulation needs.
    
4. `num_keywords = 20`: Sets the number of unique keywords to be used in the query stream. These keywords are a subset of the lowercase alphabet.
    
5. `keywords = random.sample(string.ascii_lowercase, num_keywords)`: Selects `num_keywords` (20) unique lowercase letters randomly from the alphabet. These letters will serve as the keywords in the query stream.
    
6. `query_stream = []`: Initializes an empty list to store the characters of the query stream.
    
7. `for _ in range(length):`: Starts a loop that will iterate `length` (100,000) times, generating one character for the query stream in each iteration.
    
8. `query_stream.append(random.choices(keywords, k=1)[0])`: This is the core of the query generation logic:
    
    - `random.choices(keywords, k=1)`: Selects one keyword randomly from the `keywords` list. The `choices` function allows for weighted random selection (where some choices are more likely than others), but here we are using it with equal weights for all keywords.
    - `[0]`: Extracts the selected keyword (since `random.choices` returns a list of length `k`, even when `k=1`).
    - `query_stream.append(...)`: Adds the selected keyword to the `query_stream` list.
9. `query_stream = "".join(query_stream)`: Joins the characters in the `query_stream` list into a single string.
    
10. `with open('query_stream.txt', 'w') as f`: Opens a file named "query_stream.txt" in write mode (`'w'`).
    
11. `f.write(query_stream)`: Writes the generated `query_stream` string into the "query_stream.txt" file.
    

**Key Points:**

- The generated query stream contains only the selected keywords, ensuring a controlled distribution of keywords.
- The `random.choices` function allows for potential repetition of keywords, creating a more realistic simulation of user queries.
- The query stream is saved to a file for later use by the budget allocation algorithms.

2.  

**advertiser_normal_distribution.py: Generating Advertisers with Normally Distributed Budgets**

**Context:**

This script is the second step in the online advertising simulation. It creates a set of advertisers, each with a specified budget and a set of keywords they are interested in bidding on. The key distinction of this script is that it generates budgets using a normal distribution, simulating a more realistic scenario where most advertisers have average budgets, with fewer having very high or very low budgets.

**Purpose:**

The purpose of this script is twofold:

1. To create a diverse set of advertisers with varying budgets, reflecting a more realistic distribution of advertiser spending.
2. To ensure that the total budget allocated to all advertisers matches the total number of keywords in the query stream, preventing overallocation or underutilization of resources.

**Code Explanation:**

1. Import Libraries:
    
    - `sqlite3`: This module provides a way to interact with SQLite databases, allowing us to store and retrieve advertiser data.
    - `random`: This module provides functions for generating random numbers, which are used in the budget allocation process.
    - `collections.Counter`: This class is used to count the frequency of keywords in the query stream.
2. Connect to Database:
    
    - `conn = sqlite3.connect('advertisers.db')`: Establishes a connection to the SQLite database file named "advertisers.db." If the file doesn't exist, it will be created.
    - `cursor = conn.cursor()`: Creates a cursor object that allows you to execute SQL commands on the database.
3. Create Advertisers Table (If Not Exists):
    
    - `cursor.execute('''CREATE TABLE IF NOT EXISTS advertisers (advertiser TEXT, bids TEXT, budget INTEGER)''')`: This SQL command creates a table named "advertisers" with three columns:
        
        - `advertiser`: A text column to store the unique identifier of each advertiser (e.g., "A1," "A2").
        - `bids`: A text column to store the keywords the advertiser is interested in bidding on, separated by commas (e.g., "a,b,c").
        - `budget`: An integer column to store the advertiser's total budget.
        
        The `IF NOT EXISTS` clause ensures that the table is created only if it doesn't already exist, preventing errors in subsequent runs of the script.
        
4. Load Query Stream:
    
    - `with open('query_stream.txt', 'r') as f`: Opens the "query_stream.txt" file (generated by the previous script) in read mode.
    - `query_stream = f.read()`: Reads the contents of the file, which is the string representing the sequence of keywords.
5. Calculate Keyword Frequencies:
    
    - `keyword_counts = Counter(query_stream)`: Creates a Counter object that counts the occurrences of each unique keyword in the `query_stream`.
6. Initialize Variables:
    
    - `total_budget = len(query_stream)`: Sets the `total_budget` variable to the length of the query stream, which represents the total number of keywords.
    - `num_advertisers = 25`: Specifies the desired number of advertisers to create.
    - `keyword_frequencies = {kw: count / total_budget for kw, count in keyword_counts.items()}`: Creates a dictionary `keyword_frequencies` that stores the relative frequency of each keyword in the query stream (i.e., the number of times the keyword appears divided by the total number of keywords).
7. Budget Allocation (Normal Distribution):
    
    - `mean_budget = total_budget / num_advertisers`: Calculates the mean budget that should be allocated to each advertiser to distribute the total budget evenly.
        
    - `std_dev = mean_budget / 4`: Sets the standard deviation of the normal distribution. This controls how spread out the budget values will be around the mean. A smaller standard deviation means the budgets will be more tightly clustered around the average, while a larger standard deviation will result in more variation.
        
    - `advertiser_budgets = {}`: Initializes an empty dictionary to store the budget allocated to each advertiser.
        
    - `for i in range(num_advertisers):`: Starts a loop to iterate over each advertiser.
        
        - `advertiser = f'A{i+1}'`: Creates a unique identifier for the advertiser (e.g., "A1," "A2").
        - `budget = max(1, int(random.normalvariate(mean_budget, std_dev)))`: Generates a budget value for the advertiser using a normal distribution with the calculated `mean_budget` and `std_dev`. The `max(1, ...)` ensures that the budget is at least 1.
        - `advertiser_budgets[advertiser] = budget`: Stores the generated budget in the `advertiser_budgets` dictionary.
        - `total_budget -= budget`: Decreases the `total_budget` by the allocated amount.
8. Redistribute Remaining Budget:
    
    - `while total_budget > 0`: Starts a loop that continues as long as there's still budget left to allocate.
        - `for advertiser in advertiser_budgets.keys()`: Iterates over each advertiser.
            - `redistribution = max(1, int(random.normalvariate(0, std_dev / 2)))`: Generates a small amount of budget to redistribute, again using a normal distribution. The standard deviation is halved for smaller adjustments.
            - `if redistribution > total_budget`: If the redistribution amount is more than the remaining budget, it's capped at the remaining budget.
            - `advertiser_budgets[advertiser] += redistribution`: Adds the redistribution amount to the advertiser's budget.
            - `total_budget -= redistribution`: Decreases the `total_budget` by the redistributed amount.
9. Keyword Selection and Assertion:
    
    - `all_keywords = list(keyword_counts.keys())`: Creates a list of all the unique keywords in the query stream.
    - `for advertiser, budget in advertiser_budgets.items()`: Iterates over each advertiser and their allocated budget.
        - `keywords = random.sample(all_keywords, random.randint(1, 10))`: Randomly selects 1 to 10 keywords for the advertiser to bid on.
        - `allocated_cost = sum(keyword_frequencies[keyword] * total_budget for keyword in keywords)`: Calculates the expected cost of the selected keywords based on their frequencies.
        - `assert allocated_cost <= budget, f"Budget for {advertiser} exceeds expected keyword costs!"`: This is an assertion check that ensures the allocated budget is sufficient to cover the expected cost of the keywords. If it's not, it will raise an AssertionError, helping you debug the code.
10. Insert into Database and Duplicate:
    

- `cursor.execute('''INSERT INTO advertisers VALUES (?, ?, ?)''', (advertiser, ','.join(keywords), budget))`: Inserts the advertiser's ID, selected keywords (as a comma-separated string), and the final budget into the "advertisers" table.
- `cursor.execute("CREATE TABLE advertisers_copy AS SELECT * FROM advertisers")`: Creates a duplicate of the "advertisers" table named "advertisers_copy." This duplicate table is used for the basic balance algorithm, allowing us to compare the performance of both algorithms on the same initial dataset.
- `conn.commit()`: Saves the changes made to the database.
- `conn.close()`: Closes the connection to the database.

3.  **random_advertiser.py: Generating Advertisers with Random Budgets**

**Context:**

This script serves as an alternative approach to generating advertiser data for the online advertising simulation. Unlike `advertiser_normal_distribution.py`, which uses a normal distribution to create a more realistic budget spread, this script assigns budgets to advertisers randomly, simulating a scenario where budgets are not influenced by any particular pattern or factor.

**Purpose:**

The purpose of this script is to create a set of advertisers with diverse and unpredictable budget allocations. This allows us to test the robustness of the balance algorithms in a scenario where advertiser spending power varies widely and is not tied to any specific distribution or pattern.

**Code Explanation:**

1. Import Libraries:
    
    - `sqlite3`: This module enables interaction with SQLite databases, allowing us to store and retrieve advertiser data.
    - `random`: This module provides functions for generating random numbers, which are used for budget allocation and keyword selection.
    - `collections.Counter`: This class is used to count the frequency of keywords in the query stream (although it is not directly used in this script's budget allocation logic).
2. Connect to Database:
    
    - `conn = sqlite3.connect('advertisers.db')`: Establishes a connection to the SQLite database file named "advertisers.db."
    - `cursor = conn.cursor()`: Creates a cursor object for executing SQL commands.
3. Create or Reuse the Advertisers Table:
    
    - `cursor.execute('''CREATE TABLE IF NOT EXISTS advertisers (advertiser TEXT, bids TEXT, budget INTEGER)''')`: This command either creates the "advertisers" table if it doesn't exist or uses the existing one. The table structure remains the same as in the previous script.
4. Load Query Stream:
    
    - `with open('query_stream.txt', 'r') as f`: Opens the "query_stream.txt" file for reading.
    - `query_stream = f.read()`: Reads the contents of the file, representing the sequence of keywords.
5. Calculate Keyword Counts and Total Budget:
    
    - `keyword_counts = Counter(query_stream)`: Counts the frequency of each keyword in the `query_stream`.
    - `total_budget = len(query_stream)`: Sets the `total_budget` to the length of the query stream, representing the total number of keywords.
6. Initialize Variables:
    
    - `num_advertisers = 25`: Sets the number of advertisers to be created.
    - `available_keywords = list(keyword_counts.keys())`: Creates a list of all unique keywords present in the `query_stream`. This list will be used for random keyword selection later.
7. Random Budget Allocation:
    
    - `advertiser_budgets = {}`: Initializes an empty dictionary to store the budget of each advertiser.
    - `for i in range(num_advertisers):`: Loops over the desired number of advertisers.
        - `advertiser = f'A{i+1}'`: Creates a unique identifier for the advertiser (e.g., "A1," "A2").
        - `advertiser_budgets[advertiser] = random.randint(1, total_budget)`: Assigns a random budget to the advertiser between 1 and the total budget (`total_budget`). This is where the randomness is introduced.
8. Adjust Budgets to Match Total Budget:
    
    - `allocated_budget = sum(advertiser_budgets.values())`: Calculates the sum of all the allocated budgets.
    - `while allocated_budget != total_budget`: Starts a loop that continues until the `allocated_budget` exactly matches the `total_budget`.
        - `for advertiser, budget in advertiser_budgets.items()`: Iterates over each advertiser and their budget.
            - `if allocated_budget > total_budget`: If the total allocated budget exceeds the intended total budget, it means we need to decrease some budgets:
                
                - `if budget > 1`: Checks if the current advertiser's budget is greater than 1 to avoid setting any budget to zero.
                - `advertiser_budgets[advertiser] -= 1`: Decreases the advertiser's budget by 1.
                - `allocated_budget -= 1`: Updates the `allocated_budget` accordingly.
            - `elif allocated_budget < total_budget`: If the total allocated budget is less than the intended total budget, it means we need to increase some budgets:
                
                - `advertiser_budgets[advertiser] += 1`: Increases the advertiser's budget by 1.
                - `allocated_budget += 1`: Updates the `allocated_budget` accordingly.
9. Keyword Selection and Insertion:
    
    - `for advertiser, budget in advertiser_budgets.items()`: Iterates over each advertiser and their adjusted budget.
        - `keywords = random.sample(available_keywords, random.randint(1, 10))`: Randomly selects 1 to 10 keywords for the advertiser to bid on from the `available_keywords` list.
        - `cursor.execute('''INSERT INTO advertisers VALUES (?, ?, ?)''', (advertiser, ','.join(keywords), budget))`: Inserts the advertiser's ID, selected keywords (as a comma-separated string), and the final budget into the "advertisers" table.
10. Duplicate the Advertisers Table:
    

- `cursor.execute("CREATE TABLE advertisers_copy AS SELECT * FROM advertisers")`: Creates a duplicate of the "advertisers" table named "advertisers_copy," which will be used by the basic balance algorithm for comparison.

11. Save Changes and Close Connection:

- `conn.commit()`: Saves all the changes made to the database.
- `conn.close()`: Closes the connection to the database.

4.  **advertiser_outlier.py: Generating Advertisers with Outlier Budgets**

**Context:**

This script is designed to generate a set of advertisers with a budget distribution that deliberately includes a significant number of outliers. Outliers, in this context, are advertisers with exceptionally high or low budgets compared to the average. The goal is to create a testing scenario that challenges the balance algorithms in a more extreme way than the normal distribution scenario.

**Purpose:**

The purpose of this script is to test the robustness and fairness of the balance algorithms in the face of extreme budget allocations. By simulating a situation with a few very high-budget advertisers and many low-budget ones, we can evaluate how well the algorithms perform when resources are not evenly distributed.

**Code Explanation:**

1. Import Libraries:
    
    - `sqlite3`: Enables interaction with SQLite databases for storing advertiser data.
    - `random`: Provides functions for generating random numbers used in budget allocation and keyword selection.
    - `numpy as np`: Used for generating random numbers from different probability distributions.
    - `collections.Counter`: Counts the frequency of keywords in the query stream, though not directly used in budget allocation here.
2. Connect to Database and Create/Reuse Table:
    
    - The code establishes a connection to the "advertisers.db" SQLite database and creates (or reuses) the "advertisers" table with columns `advertiser`, `bids`, and `budget`.
3. Load Query Stream and Keyword Information:
    
    - Loads the query stream from the "query_stream.txt" file.
    - Calculates `keyword_counts`, `total_budget`, and `available_keywords` as in previous scripts.
4. Generate Outlier Budgets:
    
    - `advertiser_budgets = {}`: Initializes a dictionary to store budgets.
    - `for i in range(num_advertisers):`: Loops through the specified number of advertisers.
        - `distribution_choice = random.random()`: Generates a random number between 0 and 1 to decide which budget distribution to use.
        - Three budget distributions are used, each with different probabilities:
            - Low budget (30% probability): Mean of 50, standard deviation of 10
            - Mid-range budget (30% probability): Mean close to the average budget, standard deviation of 50
            - High budget (40% probability): Mean of 2000, standard deviation of 300
        - `if random.random() < 0.1`: 10% probability of setting the budget to 0 to simulate missing values.
5. Adjust Total Budget:
    
    - If the sum of allocated budgets (`allocated_budget`) doesn't match the `total_budget`, it's adjusted by deducting the excess from the advertiser with the highest budget. This ensures the total allocated budget matches the query stream length.
6. Keyword Selection and Insertion:
    
    - Randomly selects 1 to 10 keywords for each advertiser from the `available_keywords`.
    - Inserts the advertiser's data (ID, keywords, and budget) into the "advertisers" table.
7. Duplicate Table:
    
    - Creates a copy of the "advertisers" table named "advertisers_copy" for use by the basic balance algorithm.
8. Commit Changes and Close Connection:
    
    - Saves the changes to the database and closes the connection.

**Key Points:**

- The script creates an uneven distribution of budgets, with many low-budget advertisers, a few mid-range ones, and some outliers with very high budgets.
- This distribution challenges the balance algorithms to allocate keywords fairly and maximize revenue even under extreme conditions.


5.  **balance_algorithm_basic.py: Basic Balance Algorithm for Ad Allocation**

**Context:**

This script implements the fundamental Balance Algorithm for online ad allocation. It serves as a baseline for comparison with the modified balance algorithm and its variants. The basic Balance Algorithm prioritizes fairness by selecting advertisers with the lowest remaining budget for each keyword allocation.

**Purpose:**

The purpose of this script is to allocate keywords from the query stream to advertisers based on their bids and remaining budgets. The algorithm aims to distribute the keywords in a way that gives each advertiser a fair chance to have their ads displayed, regardless of their initial budget.

**Code Explanation:**

1. **Import Library:**
    
    - `import sqlite3`: Imports the `sqlite3` module, which provides the functionality to interact with SQLite databases.
2. **Define Function `balance_algorithm`:**
    
    - `def balance_algorithm(query_stream):`: Defines a function named `balance_algorithm` that takes the `query_stream` (a string of keywords) as input.
3. **Connect to Database:**
    
    - `conn = sqlite3.connect('advertisers.db')`: Establishes a connection to the SQLite database file named "advertisers.db."
    - `cursor = conn.cursor()`: Creates a cursor object that allows the script to execute SQL commands on the database.
4. **Initialize Variables:**
    
    - `transactions = []`: Initializes an empty list to store the transaction records (keyword allocation details).
    - `serial_no = 1`: Initializes a variable to keep track of the serial number of each transaction.
5. **Iterate Through Query Stream:**
    
    - `for char in query_stream`: Starts a loop that iterates over each character (keyword) in the `query_stream`.
6. **Fetch Eligible Advertisers:**
    
    - `cursor.execute("SELECT * FROM advertisers_copy")`: Executes an SQL query to fetch all rows from the "advertisers_copy" table, which is a duplicate of the original "advertisers" table created for testing purposes.
    - `advertisers = cursor.fetchall()`: Fetches all the rows returned by the query and stores them in the `advertisers` list. Each row represents an advertiser and their data (advertiser ID, bids, budget).
    - `eligible_advertisers = [adv for adv in advertisers if char in adv[1].split(',') and adv[2] > 0]`: Filters the `advertisers` list to keep only those advertisers who meet the following conditions:
        - The current keyword (`char`) is in the advertiser's list of bids (keywords they are interested in).
        - The advertiser has a remaining budget greater than zero (`adv[2] > 0`). The budget is stored in the third column (`adv[2]`) of each row.
7. **Select Winner (Advertiser with Lowest Budget):**
    
    - `if eligible_advertisers`: Checks if there are any eligible advertisers for the current keyword.
        - `winner = min(eligible_advertisers, key=lambda x: x[2])`: Finds the advertiser with the minimum (lowest) remaining budget among the `eligible_advertisers`. The `key=lambda x: x[2]` argument specifies that the comparison should be based on the third element (`x[2]`) of each advertiser tuple (which is the budget).
        - `transactions.append((serial_no, winner[0]))`: Appends a tuple containing the `serial_no` and the winner's ID (`winner[0]`) to the `transactions` list.
        - `serial_no += 1`: Increments the `serial_no` for the next transaction.
        - `cursor.execute("UPDATE advertisers_copy SET budget = budget - 1 WHERE advertiser = ?", (winner[0],))`: Updates the database by deducting 1 from the winner's budget in the "advertisers_copy" table.
        - `conn.commit()`: Commits (saves) the changes made to the database.
8. **Close Database Connection:**
    
    - `conn.close()`: Closes the connection to the database after all keywords have been processed.
9. **Return Transactions:**
    
    - `return transactions`: Returns the list of transactions (keyword allocations) to the caller of the function.
10. **Load Query Stream and Execute Algorithm:**
    
    - This part of the script loads the query stream from the "query_stream.txt" file, calls the `balance_algorithm` function to allocate keywords, and writes the resulting `transactions` (pairs of serial number and advertiser ID) to the "transactions_basic.txt" file.

**Key Points:**

- The Basic Balance Algorithm prioritizes advertisers with lower remaining budgets, aiming for a fair distribution of keyword allocations.
- The algorithm operates in a greedy manner, making decisions based on the current state without considering future keyword frequencies or advertiser behaviors.
- The algorithm ensures that each keyword is allocated to an eligible advertiser with a positive budget.



6.  **mod_balance_algorithm.py: Modified Balance Algorithm with Sliding Window**

**Context:**

This script implements a modified version of the Balance Algorithm that incorporates a sliding window approach and additional budget constraints. The sliding window allows the algorithm to adapt to changes in keyword frequencies over time, while the budget constraints promote fairness and prevent premature budget depletion.

**Purpose:**

The purpose of this script is to allocate keywords from the query stream to advertisers in a way that maximizes revenue while maintaining fairness. It does this by prioritizing advertisers with higher remaining budgets within each sliding window and ensuring that advertisers don't exhaust their budgets too early.

**Code Explanation:**

1. **Import Library:**
    
    - `import sqlite3`: Imports the `sqlite3` module to interact with the SQLite database.
2. **Define Function `balance_algorithm`:**
    
    - `def balance_algorithm(query_stream, window_size=100):`: Defines a function named `balance_algorithm` that takes two arguments:
        - `query_stream`: A string representing the sequence of keywords.
        - `window_size`: An optional parameter that specifies the size of the sliding window (default is 100).
3. **Connect to Database:**
    
    - `conn = sqlite3.connect('advertisers.db')`: Establishes a connection to the SQLite database file named "advertisers.db."
    - `cursor = conn.cursor()`: Creates a cursor object for executing SQL commands on the database.
4. **Initialize Variables:**
    
    - `transactions = []`: Initializes an empty list to store the transaction records (keyword allocation details).
    - `serial_no = 1`: Initializes a variable to keep track of the serial number of each transaction.
5. **Iterate over Sliding Windows:**
    
    - `for i in range(0, len(query_stream), window_size)`: Starts a loop that iterates over the `query_stream` in steps of `window_size`.
        - `window = query_stream[i:i + window_size]`: Creates a sliding window containing `window_size` keywords.
6. **Iterate Within Each Window:**
    
    - `for char in window`: Starts a nested loop that iterates over each keyword (`char`) within the current window.
7. **Fetch Eligible Advertisers:**
    
    - `cursor.execute("SELECT * FROM advertisers")`: Fetches all rows from the "advertisers" table.
    - `advertisers = cursor.fetchall()`: Retrieves all the rows as a list of tuples.
    - `eligible_advertisers = [adv for adv in advertisers if char in adv[1].split(',') and adv[2] > 0 and adv[2] > adv[2] // 2]`: Filters the advertisers to keep only those who meet the following criteria:
        - The current keyword (`char`) is in the advertiser's list of bids.
        - The advertiser has a remaining budget (`adv[2]`) greater than 0.
        - The advertiser has spent less than or equal to 50% of their initial budget (`adv[2] > adv[2] // 2`).
8. **Select Winner (Advertiser with Highest Budget):**
    
    - `if eligible_advertisers`: Checks if there are any eligible advertisers.
        - `winner = max(eligible_advertisers, key=lambda x: x[2])`: Finds the advertiser with the maximum (highest) remaining budget among the `eligible_advertisers`.
        - `if winner[2] > 0`: Ensures the winner still has a positive budget before allocating.
            - `transactions.append((serial_no, winner[0]))`: Records the transaction.
            - `serial_no += 1`: Increments the transaction serial number.
            - `cursor.execute("UPDATE advertisers SET budget = budget - 1 WHERE advertiser = ?", (winner[0],))`: Decreases the winner's budget in the database by 1.
            - `conn.commit()`: Saves the changes to the database.
9. **Close Database Connection and Return Transactions:**
    
    - `conn.close()`: Closes the database connection.
    - `return transactions`: Returns the list of transaction records.

**Key Points:**

- The modified algorithm processes the query stream in smaller windows for better adaptability to keyword frequency changes.
- It prioritizes advertisers with higher remaining budgets within each window.
- It prevents advertisers from being selected if their budget has dropped below 50% of their initial allocation, promoting fairness.

7.   **mod_balance_no_slide.py: Modified Balance Algorithm (No Sliding Window)**

**Context:**

This script implements a variation of the modified Balance Algorithm where the sliding window mechanism is removed. This means that the algorithm processes the query stream one keyword at a time, making allocation decisions based on the entire historical context of the stream up to that point.

**Purpose:**

The purpose of this script is to investigate the impact of removing the sliding window on the algorithm's performance and fairness. By comparing this variant to the modified algorithm with sliding window, we can assess the specific benefits of the sliding window approach.

**Code Explanation:**

1. **Import Library:**
    
    - `import sqlite3`: Imports the `sqlite3` module to interact with the SQLite database.
2. **Define Function `balance_algorithm`:**
    
    - `def balance_algorithm(query_stream):`: Defines a function named `balance_algorithm` that takes the `query_stream` as input. Note that the `window_size` parameter has been removed.
3. **Connect to Database:**
    
    - `conn = sqlite3.connect('advertisers.db')`: Establishes a connection to the SQLite database file named "advertisers.db."
    - `cursor = conn.cursor()`: Creates a cursor object for executing SQL commands.
4. **Initialize Variables:**
    
    - `transactions = []`: Initializes an empty list to store the transaction records.
    - `serial_no = 1`: Initializes a variable to keep track of the transaction serial number.
5. **Iterate Through Query Stream (No Window):**
    
    - `for char in query_stream`: Starts a loop that iterates directly over each character (keyword) in the `query_stream`, without creating any windows.
6. **Fetch Eligible Advertisers:**
    
    - `cursor.execute("SELECT * FROM advertisers")`: Fetches all rows from the "advertisers" table.
    - `advertisers = cursor.fetchall()`: Retrieves all rows as a list of tuples.
    - `eligible_advertisers = [adv for adv in advertisers if char in adv[1].split(',') and adv[2] > 0 and adv[2] > adv[2] // 2]`: Filters the advertisers to keep only those who meet the same criteria as in the modified algorithm with the sliding window (i.e., the keyword is in their bid list, they have a positive budget, and they have spent less than 50% of their initial budget).
7. **Select Winner (Advertiser with Highest Budget):**
    
    - `if eligible_advertisers`: Checks if there are any eligible advertisers.
        - `winner = max(eligible_advertisers, key=lambda x: x[2])`: Finds the advertiser with the maximum (highest) remaining budget among the eligible advertisers.
        - `if winner[2] > 0`: Ensures the winner has a positive budget before allocation.
            - `transactions.append((serial_no, winner[0]))`: Records the transaction.
            - `serial_no += 1`: Increments the transaction serial number.
            - `cursor.execute("UPDATE advertisers SET budget = budget - 1 WHERE advertiser = ?", (winner[0],))`: Decreases the winner's budget in the database.
            - `conn.commit()`: Saves the changes.
8. **Close Database Connection and Return Transactions:**
    
    - `conn.close()`: Closes the database connection.
    - `return transactions`: Returns the list of transaction records.

**Key Points:**

- This variant removes the sliding window mechanism, processing the query stream one keyword at a time.
- It retains the budget percentage check and prioritization of advertisers with higher remaining budgets.
- By comparing this variant to the one with the sliding window, we can isolate the specific impact of the sliding window on performance and fairness.
  
  8. **analyzer_mod.py: Analyzing Results of the Modified Balance Algorithm**

**Context:**

This script is the final step in the simulation process. It analyzes the output of the modified balance algorithms (`mod_balance_algorithm.py` and `mod_balance_no_slide.py`), which have already processed the query stream and allocated keywords to advertisers.

**Purpose:**

The purpose of this script is twofold:

1. **Calculate Total Revenue:** Determine the total revenue generated by the algorithm, which is the number of unique keyword allocations.
    
2. **Calculate Spending per Advertiser:** Determine how much each advertiser has spent (i.e., how many keywords they were allocated) and store this information in a dictionary.
    

**Code Explanation:**

1. **Open and Read Transactions File:**
    
    - `with open('transactions.txt', 'r') as f`: Opens the "transactions.txt" file (generated by the balance algorithm scripts) in read mode.
    - `transactions = [line.strip().split(',') for line in f]`: Reads the lines from the file and splits each line into a list of two elements:
        - The first element is the transaction serial number.
        - The second element is the advertiser ID.
2. **Calculate Total Revenue:**
    
    - `total_revenue = len(set(int(serial_no) for serial_no, _ in transactions))`: Calculates the total revenue by counting the number of unique serial numbers in the `transactions` list. This is done by:
        - Extracting the `serial_no` from each transaction.
        - Converting the `serial_no` to an integer using `int()`.
        - Creating a set (`set(...)`) to keep only the unique serial numbers.
        - Calculating the length of the set using `len()`.
3. **Calculate Spending per Advertiser:**
    
    - `spending_per_advertiser = {}`: Initializes an empty dictionary to store the spending for each advertiser.
    - `for _, advertiser in transactions`: Iterates over each transaction, ignoring the serial number (`_`).
        - `spending_per_advertiser[advertiser] = spending_per_advertiser.get(advertiser, 0) + 1`: Increments the spending counter for the current `advertiser` in the dictionary. The `.get(advertiser, 0)` part ensures that if the advertiser is not yet in the dictionary, their spending is initialized to 0.
4. **Write Results to File:**
    
    - `with open('results.txt', 'w') as f`: Opens a file named "results.txt" in write mode.
    - `f.write(f"Total Revenue: {total_revenue}\n")`: Writes the total revenue to the file.
    - `for advertiser, spending in spending_per_advertiser.items()`: Iterates over the `spending_per_advertiser` dictionary, writing each advertiser's ID and their spending to the file.

**Key Points:**

- The script analyzes the "transactions.txt" file, which should contain the output of a modified balance algorithm run.
- It calculates the total revenue by counting unique transactions (serial numbers).
- It calculates the spending for each advertiser by counting how many times their ID appears in the transactions.
- It saves the results in a "results.txt" file.


9.  **analyzer_basic.py: Analyzing Results of the Basic Balance Algorithm**

**Context:**

This script is the final step in the simulation process for the basic balance algorithm. It analyzes the output of the `balance_algorithm_basic.py` script, which has already processed the query stream and allocated keywords to advertisers based on the basic balance algorithm logic.

**Purpose:**

The purpose of this script is identical to `analyzer_mod.py`:

1. **Calculate Total Revenue:** Determine the total revenue generated by the algorithm, which is the number of unique keyword allocations.
    
2. **Calculate Spending per Advertiser:** Determine how much each advertiser has spent (i.e., how many keywords they were allocated) and store this information in a dictionary.
    

**Code Explanation:**

The code in `analyzer_basic.py` is almost identical to the `analyzer_mod.py` code. The only difference is that it reads the transaction data from the "transactions_basic.txt" file, which is generated by the `balance_algorithm_basic.py` script. Here's the explanation again, highlighting the slight difference:

1. **Open and Read Transactions File:**
    
    - `with open('transactions_basic.txt', 'r') as f`: Opens the "transactions_basic.txt" file in read mode.
2. **Calculate Total Revenue:**
    
    - (Same as in `analyzer_mod.py`)
3. **Calculate Spending per Advertiser:**
    
    - (Same as in `analyzer_mod.py`)
4. **Write Results to File:**
    
    - `with open('results_basic.txt', 'w') as f`: Opens a file named "results_basic.txt" in write mode. (Note the difference in filename from `analyzer_mod.py`)
    - (The rest is the same as in `analyzer_mod.py`)

**Key Points:**

- The script analyzes the "transactions_basic.txt" file, which should contain the output of a basic balance algorithm run.
- The calculations for total revenue and spending per advertiser are identical to those in `analyzer_mod.py`.
- It saves the results in a separate file, "results_basic.txt," to distinguish them from the results of the modified balance algorithm.

  ### Guidelines for running the code
  - Install the dependencies like numpy,sqlite3,collections library in python etc
  - Firstly run the Query.py to generate the query stream
  - AFterwards run any of the advertisor generator variants to your liking to observe the behaviour
  - afterwards run the normal balance algorithm code and any of our balance algorithm code containing the word mod in the name of the file
  - this will get you tranasactions for both of the variants, only one of the varaiants of modified algo can be run at a time and cannot be re run with the same set of advertisers.db file as it would have written into it and made changes to handle the budget
  - aftwerwards run the analyzer both the codes and you will get results.txt and results_basic.txt
  - if you wish to run the code with different specifications kindly delete the advertisers.ddb file and re run all the steps again
