# adaptive-ad-budget-allocator
**Project Title:** Adaptive and Fair Resource Allocation Algorithm for Scalable Online Advertising

**Truth Bombs and Confessions: Journey Behind this Repo**

Initially, this project aimed to develop and enhance a modified Balance Algorithm for more effective online advertising budget allocation. My goal was to surpass the basic Balance Algorithm's performance, ensuring better fairness and adaptability for real-world advertiser behaviors and keyword distributions. However, after months of intense brainstorming, scripting, and testing, I realized that modifying the original Balance Algorithm—both theoretically and mathematically—was not feasible. Despite this, the technical insights gained throughout the journey were invaluable. I ultimately replaced all custom scripts, updating the repository to implement and evaluate the original Balance Algorithm.

**Project Overview:**

1.  **Basic Balance Algorithm Implementation:**
    *   The project began with the implementation of the basic Balance Algorithm, which prioritizes advertisers with the lowest remaining budget for each keyword allocation.
    *   This served as the baseline for comparison and performance evaluation.

2.  **Query Stream and Advertiser Generation:**
    *   A query stream generator was created to simulate user queries, initially with a random distribution of keywords.
    *   An advertiser generator was developed to randomly assign budgets and bidding keywords to a set of advertisers.

3.  **Scenario Variations:**
    *   The query stream generator was modified to create different scenarios:
        *   **Average Case:** Keyword frequencies followed a more realistic distribution (e.g., normal or Poisson distribution) with some overlap between advertisers' bids.
        *   **Random Case:** Budgets were allocated completely randomly, simulating an extreme edge case.
        *   **Outlier-Heavy Case:** Budgets were generated with a significant number of outliers (very high or very low) to test the algorithm's robustness.

4.  **Experimentation and Analysis:**
    *   Both the modified and basic balance algorithms were tested on various query stream and budget allocation scenarios.
    *   Results were analyzed in terms of total revenue generated and the distribution of spending across advertisers.

**Key Findings:**

*   **Fairer Distribution:** The algorithm achieved a more balanced distribution of keywords among advertisers, reducing the bias towards advertisers with lower budgets.
*   **Adaptability:** The algorithm demonstrated better adaptability to changing keyword frequencies due to the sliding window mechanism.
*   **Robustness:** The modified algorithm remained effective even in the outlier-heavy scenario, showing its resilience to extreme budget distributions.

## Running the project

1. Run the Query generation script.
```
python3 Query.py
```
2. Run any one out of 3 advertisers - normal, random, outlier (heavy) script.
```
python3 <any one>
```
3. Run the balance_algorithm_basic.py 
```
python3 balance_algorithm_basic.py
```
4. Run the final analyser which provides comprehensive results.
```
python3 analyzer_basic.py
```

## Results
This algorithm provides comprehensive results in very less computation time in random, normal and heavy case scenarios, experimentally. An example of results under normal distribution is shown below.

```
Total Revenue: 99805
A9: 5007
A20: 5070
A8: 5967
A4: 4453
A16: 4762
A10: 4630
A6: 4726
A19: 4923
A12: 4721
A24: 4599
A21: 4448
A18: 4336
A23: 4129
A25: 3995
A1: 3966
A5: 3738
A2: 3715
A17: 3681
A15: 3267
A13: 3115
A22: 2876
A7: 2797
A3: 2509
A14: 2319
A11: 2056
```
