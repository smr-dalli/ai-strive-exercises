<h1 align="center">Day 2: Data Cleaning (Missings and Outliers)</h1>

## Exercises

### ❓ Missing values

1. What is the missing datatype used in pandas?
Ans: np.NaN,empty strings and constants. 

2. How to replace all occurences of the value 9999 to missing in pandas?
Ans: Replace the 9999 to np.NaN

3. How to get the absolute number of missings for each variable in pandas?
Ans: df.column.isna().sum()

4. How to get the percentage of missings for each variable in pandas?
Ans: df.column_name.isna().sum() / len(df.column_name)

5. How to drop rows with missing values?
Ans: 1. Directly drop the rows with missing values. df.dropna(axis = 1)
     2. Imputation.
     from Sklearn import impute.SimpleImputer(strategy = ['constant','mean','median','most frequent'])
     Also, for constant, replace the value with out of feature range such as num: -999,-1,cat: 'missing_value'.
     3. Using Model such as XGBoost,LightGBM

6. How to drop variables with missing values?
Ans: 1. Directly drop the rows with missing values. df.dropna(axis = 0)
     2. Imputation.
     from Sklearn import impute.SimpleImputer(strategy = ['constant','mean','median','most frequent'])
     Also, for constant, replace the value with out of feature range such as num: -999,-1,cat: 'missing_value'.
     3. Using Model such as XGBoost,LightGBM

7. What is the univariate imputation method in sklearn?
Ans: 1. Imputation.
     from Sklearn import impute.SimpleImputer(strategy = ['constant','mean','median','most frequent'])
     Also, for constant, replace the value with out of feature range such as num: -999,-1,cat: 'missing_value'.
     2. Using Model such as XGBoost,LightGBM

8. What is the multivariate imputation method in sklearn?
Ans: In the multivariate, we reconstruct the missing values based on the other variables.
     In, Scikit learn, we use impute.iterativeImputer() and impute.KNNimputer()

9. What is the best univariate imputation method to categorical variables? (Explain why)
Ans: Using the strategy, Replace the value with 'missing_value'

10. What is the best univariate imputation method to numerical variables? (Explain why)
Ans: Using the strategy, Replace the misising value with mean.
     Also, for Tree models, replacing with value that is out of range feature value such as -999,-1.


### 🔎 Outliers

1. What is an outlier?
Ans: An outlier is a data point that differs significantly from the actual observations. 

2. What is a simple method to detect and deal with outliers of a numerical variable?
Ans: We must remove otliers for the model accuracy. Plotting the distribution plot is the efficient method.

3. What is novelty detection?
Ans: Novelty detection is the task of classifying test data that differ in some respect from the data that are
 available during training

4. Name 4 advanced methods of outlier detection in sklearn.
Ans: Robust Covariance
     One Class svm
     Isolation Forest
     Local outlier factor


### 🖋 Typos

1. What is a typo?
Ans: Errors during the data entry. Detection of the typos and correcting it must be done.

2. What is a good method of automatically detect typos?
Ans: Using FuzzyWuzzy that identifies typos automatically and fixes it.



### Practical case

Consider the following dataset: [San Francisco Building Permits](https://www.kaggle.com/aparnashastry/building-permit-applications-data). Look at the columns "Street Number Suffix" and "Zipcode". Both of these contain missing values.

- Which, if either, are missing because they don't exist?
- Which, if either, are missing because they weren't recorded?

Hint: Do all addresses generally have a street number suffix? Do all addresses generally have a zipcode?

Ans: 
Code:
miss_val = df['Street Number Suffix'].isna().sum() / len(df)
print(f'Missing value percentage of Street Number Suffix column is:{round(miss_val*100,2)}')
missing_val = df['Zipcode'].isna().sum() / len(df)
print(f'Missing value percentage of Zipcode column is:{round(missing_val*100,2)}')

Result: 
Missing value percentage of Street Number Suffix column is:98.89
Missing value percentage of Zipcode column is:0.86

Conclusion:
There are a lot of missing values in Street Number Suffix column, There exists few suffix but not recorded.
They were not recorded in Zipcode column.



| Var # |  NaN % | Var name                               | Var Description                                    |
|------:|-------:|:---------------------------------------|:---------------------------------------------------|
|     1 |      0 | Permit Number                          | Number assigned while filing                       |
|     2 |      0 | Permit Type                            | Type of the permit represented numerically.        |
|     3 |      0 | Permit Type Definition    | Description of the Permit type, for example new construction, alterations |
|     4 |      0 | Permit Creation Date      | Date on which permit created, later than or same as filing date           |
|     5 |      0 | Block                                  | Related to address                                 |
|     6 |      0 | Lot                                    | Related to address                                 |
|     7 |      0 | Street Number                          | Related to address                                 |
|     8 | 98.885 | **Street Number Suffix**               | Related to address                                 |
|     9 |      0 | Street Name                            | Related to address                                 |
|    10 |  1.391 | Street Name Suffix                     | Related to address                                 |
|    11 | 85.178 | Unit                                   | Unit of a building                                 |
|    12 | 99.014 | Unit suffix                            | Suffix if any, for the unit                        |
|    13 |  0.145 | Description         | Details about purpose of the permit. Example: reroofing, bathroom renovation     |
|    14 |      0 | Current Status                         | Current status of the permit application.          |
|    15 |      0 | Current Status Date                    | Date at which current status was entered           |
|    16 |      0 | Filed Date                             | Filed date for the permit                          |
|    17 |  7.511 | Issued Date                            | Issued date for the permit                         |
|    18 | 51.135 | Completed Date  | The date on which project was completed, applicable if Current Status = “completed”   |
|    19 |  7.514 | First Construction Document Date       | Date on which construction was documented          |
|    20 | 96.519 | Structural Notification                | Notification to meet some legal need, given or not |
|    21 | 21.510 | Number of Existing Stories | Num of existing stories in the building. Not applicable for certain permit types|
|    22 | 21.552 | Number of Proposed Stories             | Number of proposed stories for the construction/alteration    |
|    23 | 99.982 | Voluntary Soft-Story Retrofit          | Soft story to meet earth quake regulations      |
|    24 | 90.534 | Fire Only Permit                       | Fire hazard prevention related permit           |
|    25 | 26.083 | Permit Expiration Date                 | Expiration date related to issued permit.       |
|    26 | 19.138 | Estimated Cost                         | Initial estimation of the cost of the project   |
|    27 |  3.049 | Revised Cost                           | Revised estimation of the cost of the project   |
|    28 | 20.670 | Existing Use                           | Existing use of the building                    |
|    29 | 25.911 | Existing Units                         | Existing number of units                        |
|    30 | 21.336 | Proposed Use                           | Proposed use of the building                    |
|    31 | 25.596 | Proposed Units                         | Proposed number of units                        |
|    32 | 18.757 | Plansets        | Plan representation indicating the general design intent of the foundation..            |
|    33 | 99.998 | TIDF Compliance                        | TIDF compliant or not, this is a new legal requirement           |
|    34 | 21.802 | Existing Construction Type         | Construction type, existing,as categories represented numerically    |
|    35 | 21.802 | Existing Construction Type Description | Descr. of the above, eg.: wood or other construction types       |
|    36 | 21.700 | Proposed Construction Type         | Construction type, proposed, as categories represented numerically   |
|    37 | 21.700 | Proposed Construction Type Description | Description of the above                                         |
|    38 | 97.305 | Site Permit                            | Permit for site                                                  |
|    39 |  0.863 | Supervisor District                    | Supervisor District to which the building location belongs to    |
|    40 |  0.867 | Neighborhoods - Analysis Boundaries    | Neighborhood to which the building location belongs to           |
|    41 |  0.862 | **Zipcode**                            | Zipcode of building address                                      |
|    42 |  0.854 | Location                               | Location in latitude, longitude pair.                            |
|    43 |      0 | Record ID                              | Some ID, not useful for this                                     |


## Optional External Exercises:

From Kaggle [data cleaning mini course](https://www.kaggle.com/learn/data-cleaning) do:
- [Handling Missing Values](https://www.kaggle.com/alexisbcook/handling-missing-values) Data Cleaning: 1 of 5
- [Inconsistent Data Entry](https://www.kaggle.com/alexisbcook/inconsistent-data-entry) Data Cleaning: 5 of 5
