# Project 2: Data Analysis of HDB Resale Prices

Prepared by Maimunah Binte Iskhander, 1 Sept 2023

### Overview
This project uses Exploratory Data Analysis (EDA) and Linear Regression to predict the price of resale HDB flats based on the HDB dataset from March 2012 to April 2021. The models used are Linear Regression, ElasticNet and Polynomial Regression with either Ridge or Lasso Regularisation.

### Problem Statement
Even though HDB aims for affordable housing, prices still vary a lot between different areas. This seems to go against what HDB is trying to achieve. To help fix this, we plan to work on making prices more balanced across the board. Our goal is to utilize data analytics to identify which amenities most significantly contribute to higher property prices. This will help the government use its resources more efficiently to improve the value of homes that are currently seen as less desirable.

### Evaluation
Models will be evaluated using the root mean squared error (RMSE). As an added measure, the R2 scores will also be calculated.

### Datasets
Datasets provided: 
* [`train.csv`](./datasets/train.csv): Training data. HDB resale flat transactions between March 2012 and April 2021.
* [`test.csv`](./dataset/test.csv): Testing data. HDB resale flat transactions between March 2012 and April 2021 without the target variable.

#### Data dictionary
| Feature                  | Type    | Description                                                                 |
|--------------------------|---------|-----------------------------------------------------------------------------|
| floor_area_sqm           | Float   | Floor area of the resale flat unit in square metres                         |
| mall_nearest_distance    | Float   | Distance (in metres) to the nearest mall                                    |
| mrt_nearest_distance     | Float   | Distance (in metres) to the nearest MRT station                             |
| pri_sch_nearest_distance | Float   | Distance (in metres) to the nearest primary school                          |
| hawker_food_stalls       | Integer | Number of hawker food stalls in the nearest hawker centre                   |
| hawker_market_stalls     | Integer | Number of hawker and market stalls in the nearest hawker centre             |
| market_hawker            | Integer | Boolean value if resale flat has a market or hawker centre in the same block|
| tranc_year               | Integer | Year of resale transaction                                                  |
| max_floor_lvl            | Integer | Highest floor of the resale flat                                            |
| cutoff_point             | Integer | PSLE cutoff point of the nearest secondary school                           |
| mid                      | Integer | Middle value of storey_range                                                |
| hdb_age                  | Integer | Number of years from lease_commence_date to present year                    |
| multistorey_carpark      | Integer | Boolean value if resale flat has a multistorey carpark in the same block    |
| town                     | Object  | HDB township where the flat is located                                      |
| commercial               | Object  | Boolean value if resale flat has commercial units in the same block         |
| pri_sch_name             | Object  | Name of the nearest primary school                                          |
| sec_sch_name             | Object  | Name of the nearest secondary school                                        |
| flat_type                | Object  | Type of the resale flat unit                                                |
| flat_model               | Object  | HDB model of the resale flat                                                |
| planning_area            | Object  | Government planning area that the flat is located                           |

### Submissions
Files submitted: 
* [`Part1.ipynb`](./code/Part1.ipynb): Data Cleaning & Preparation
* [`Part2.ipynb`](./code/Part2.ipynb): EDA 
* [`Part3.ipynb`](./code/Part3.ipynb): Preprocessing, Modelling & Kaggle Submission
* [`Project_2_slides.pdf`](./slides/Project_2_slides.pdf): Group presentation slides

### Summary
A Polynomial Ridge Regression model based on 14 features (Feature D) was chosen as the best model.

|Metric    |Train     |Test      |
|:--------:|:--------:|:--------:|
|RMSE      |28295     |28849     |
|R2 score  |0.939     |0.937     |

Root Mean Squared Error (Train): 28295.012401304946
Root Mean Squared Error (Test): 28849.558755472237

R2 Score (Train): 0.9396634952399943
R2 Score (Test): 0.9373571489171859

There are no signs of overfitting. 

**Top 3 Drivers**
1. MRT nearest distance
2. Commercial
3. Hawker_Market

### Recommendations
The chosen model is able to predict the prices of HDB resale flats with an RMSE of 28765 and an R2 score of 0.937. 

It is recommended that MRTs are built closer to new estates so that these can fetch higher prices, reduce the number of commercial units in a HDB estate and continue to build more hawker and market stalls in HDB estates.

### Area for Improvements
- Collect more training data 
- Adjust prices for inflation 
- Add more features such as state of resale flat i.e. does it require extensive renovation
- Find an optimal value for KFold
- Feature engineering using interaction terms