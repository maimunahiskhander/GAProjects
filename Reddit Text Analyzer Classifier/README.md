# Project 3: Reddit Classifier - Netflix or Disney Plus

Prepared by: Maimunah Binte Iskhander, 29 Sept 2023

### Overview

This project employs Exploratory Data Analysis (EDA) and various classification models to predict whether a given text originates from a Netflix subreddit or a Disney Plus subreddit. The models explored include Logistic Regression, Multinomial Naive Bayes, Random Forest, AdaBoost, and XGBoost. The text data is vectorized using either CountVectorizer or TfidfVectorizer.

### Problem Statement

Netflix aims to launch a marketing campaign that utilizes keywords and themes commonly associated with Disney+ in order to divert more online search traffic to their platform.

### Evaluation Criteria

Given the nature of the data and its potential class imbalance, models will be evaluated based on their F1 score.

### Datasets

Scraped Datasets: 
* [`Netflix_reddit_submissions.csv`](./datasets/Netflix_reddit_submissions.csv): Netflix subreddit data retrieved on 26 Sept 2023.
* [`DisneyPlus_reddit_submissions.csv`](./dataset/DisneyPlus_reddit_submissions.csv): Disney Plus subreddit data retrieved on 26 Sept 2023.

### Data Dictionary

| Variable Name         | Data Type           | Description                                   |
|-----------------------|---------------------|-----------------------------------------------|
| `post_id`             | object              | Unique identifier for the submission          |
| `title`               | object              | Title of the submission                       |
| `selftext`            | object              | Body text of the submission                   |
| `ups`                 | int64               | Number of upvotes received by the submission  |
| `upvote_ratio`        | float64             | Ratio of upvotes to total votes               |
| `num_comments`        | int64               | Number of comments on the submission          |
| `author`              | object              | Author's username                             |
| `link_flair_text`     | object              | Flair text associated with the submission     |
| `awards`              | int64               | Number of awards received by the submission   |
| `is_original_content` | bool                | Whether the content is original               |
| `is_video`            | bool                | Whether the submission is a video             |
| `post_type`           | object              | Type of the post (either text or link)        |
| `domain`              | object              | Domain associated with the submission link    |
| `created_utc`         | float64             | UTC timestamp when the submission was created |
| `pinned`              | bool                | Whether the submission is pinned              |
| `locked`              | bool                | Whether the submission is locked              |
| `stickied`            | bool                | Whether the submission is stickied            |
| `readable_time`       | datetime64[ns]      | Readable timestamp of the submission           |


### Submissions
Files submitted: 
* [`Project_3_Part_1.ipynb`](./code/Project_3_Part_1.ipynb): This notebook covers Data Scraping, Problem Statement formulation, and Research.
* [`Project_3_Part_2.ipynb`](./code/Project_3_Part_2.ipynb): This notebook delves into Data Cleaning, Preprocessing, EDA, Model Building, Hyperparameter Tuning, and Key Findings.
* [`Project_3_slides.pdf`](./slides/Project_3_slides.pdf): Presentation slides for the project.

### Summary
The Multinomial Naive Bayes model, paired with TfidfVectorizer, was determined to be the most effective model. The model's hyperparameters are:

| Parameter                    | Value                                                      |
|------------------------------|------------------------------------------------------------|
| `classifier`                 | MultinomialNB(alpha=0.1)                                   |
| `classifier__alpha`          | 0.1                                                        |
| `vectorizer`                 | TfidfVectorizer(max_df=0.9, max_features=12000, min_df=2, ngram_range=(1, 2)) |
| `vectorizer__max_df`         | 0.9                                                        |
| `vectorizer__max_features`   | 12000                                                      |
| `vectorizer__min_df`         | 2                                                          |
| `vectorizer__ngram_range`    | (1, 2)                                                     |

The model's performance was assessed using the F1 score, with the following outcomes:


|Metric    |Train     |Test      |
|:--------:|:--------:|:--------:|
|F1 Score  |0.9858	  |0.9369    |


The train-test score difference is 4.8%, which falls within the acceptable 10% threshold, indicating a mild overfitting.

### Key Findings

1. Common words such as "app", "look", "good", "want", "time", "think", "episode", "movie", "like", and "watch" appear frequently in both subreddits. This suggests topics of mutual interest across both streaming services.
2. The presence of words like "bad" and "cancel" might highlight some users' dissatisfaction or issues with Netflix.
3. Distinct themes associated with DisneyPlus are indicated by words like "star wars", "marvel", and "hulu".
4. Both subreddits contain discussions about platform functionalities and user experiences. This underscores the importance users place on the user interface, features, and overall experience of the streaming platforms.

### Business Recommendations

1. Leverage Popular Disney Themes: Netflix could consider securing or creating content that aligns with popular themes on DisneyPlus, such as the sci-fi or superhero genres. This strategy could attract viewers desiring content variety.
2. Enhance User Experience: Netflix should prioritize user experience by ensuring a user-friendly interface and continuously upgrading platform features.
3. Content Marketing: Highlighting unique Netflix content can be a strategic move to attract or retain viewers.

### Areas for Improvement

1. Data Expansion: More data over a longer period can provide robustness to the model.
2. Sentiment Analysis: Integrate sentiment scores as features for a deeper understanding of user sentiment.
3. Model Exploration: Consider advanced models, including deep learning, for text classification.
4. Ensemble Methods: Combining predictions from various models might improve accuracy.
5. Addressing Cleaning Pitfalls: Ensure that automated cleaning doesn't lead to artifacts like long strings of words.


