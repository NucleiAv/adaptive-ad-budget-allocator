# adaptive-ad-budget-allocator
**Project Title:** Adaptive and Fair Resource Allocation Algorithm for Scalable Online Advertising

**Project Overview:**

The project aimed to develop and evaluate a modified Balance Algorithm for online advertising budget allocation. The primary goal was to improve upon the basic Balance Algorithm's performance, fairness, and adaptability in real-world scenarios with diverse advertiser behaviors and keyword distributions. This project has a modified and optimised algorithm with proper results. Read project.md for concrete results and explanations.

**Development Steps:**

1.  **Basic Balance Algorithm Implementation:**
    *   The project began with the implementation of the basic Balance Algorithm, which prioritizes advertisers with the lowest remaining budget for each keyword allocation.
    *   This served as the baseline for comparison and performance evaluation.

2.  **Modified Balance Algorithm Development:**
    *   Several key modifications were introduced to address limitations of the basic algorithm:
        *   **Sliding Window:** The query stream was processed in smaller chunks (windows) to allow dynamic adaptation to changing keyword frequencies.
        *   **Budget Percentage Check:** A constraint was added to prevent advertisers with less than 50% of their budget remaining from being selected, ensuring fair distribution of opportunities.
        *   **Keyword-Frequency Based Budget Allocation:** Advertiser budgets were initially allocated proportionally based on the frequency of the keywords they bid on.
        *   **Normal Distribution and Redistribution:**  The initial budget allocation was refined using a normal distribution and redistribution mechanisms to create a more balanced and fair distribution of resources.
        *   **Excess Budget Deduction:**  Any remaining budget was deducted from the advertiser with the highest budget, ensuring full budget utilization.

3.  **Query Stream and Advertiser Generation:**
    *   A query stream generator was created to simulate user queries, initially with a random distribution of keywords.
    *   An advertiser generator was developed to randomly assign budgets and bidding keywords to a set of advertisers.

4.  **Scenario Variations:**
    *   The query stream generator was modified to create different scenarios:
        *   **Average Case:** Keyword frequencies followed a more realistic distribution (e.g., normal or Poisson distribution) with some overlap between advertisers' bids.
        *   **Random Case:** Budgets were allocated completely randomly, simulating an extreme edge case.
        *   **Outlier-Heavy Case:** Budgets were generated with a significant number of outliers (very high or very low) to test the algorithm's robustness.

5.  **Experimentation and Analysis:**
    *   Both the modified and basic balance algorithms were tested on various query stream and budget allocation scenarios.
    *   Results were analyzed in terms of total revenue generated and the distribution of spending across advertisers.

**Key Findings:**

*   **Superior Performance of Modified Algorithm:** The modified balance algorithm consistently outperformed the basic balance algorithm in all tested scenarios.
*   **Increased Revenue:** The modified algorithm generated significantly higher revenue compared to the basic algorithm, even in the completely random budget allocation scenario.
*   **Fairer Distribution:** The modified algorithm achieved a more balanced distribution of keywords among advertisers, reducing the bias of the basic algorithm towards advertisers with lower budgets.
*   **Adaptability:** The modified algorithm demonstrated better adaptability to changing keyword frequencies due to the sliding window mechanism.
*   **Robustness:** The modified algorithm remained effective even in the outlier-heavy scenario, showing its resilience to extreme budget distributions.

**Conclusion:**

This project successfully developed and validated a modified Balance Algorithm for online advertising budget allocation. The algorithm incorporates several key enhancements that address limitations of the basic Balance Algorithm and lead to improved revenue generation, fairness, and adaptability in various scenarios. These results suggest that the modified algorithm has the potential to significantly enhance the effectiveness and efficiency of online advertising platforms.

**Code Snippets (Key Modifications):**

python
# In advertiser_generator.py:

# Initial budget allocation using normal distribution (for average case)
mean_budget = total_budget / num_advertisers
std_dev = mean_budget / 4  # Adjust for desired distribution spread

advertiser_budgets = {}
for i in range(num_advertisers):
    advertiser = f'A{i+1}'
    budget = max(1, int(random.normalvariate(mean_budget, std_dev)))
    advertiser_budgets[advertiser] = budget
    total_budget -= budget

# ... (Redistribution and other modifications)


python
# In balance_algorithm.py (Modified):
for i in range(0, len(query_stream), window_size):
    window = query_stream[i:i + window_size]  # Sliding window

    for char in window:
        # ... (Algorithm logic with budget and spending checks)


I hope this comprehensive report provides a clear and detailed overview of the project, its findings, and the improvements made to the algorithm. Please let me know if you have any further questions or requests!
