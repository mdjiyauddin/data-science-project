import pandas as pd
import numpy as np

# Correct path format (raw string)
df = pd.read_csv(r'numpy or pandas project\employees_100.csv')

#  Display missing values summary
print("Missing values in each column before cleaning:\n")
print(df.isnull().sum())


#  NUMERIC DATA CLEANING

df['salary_inr'].fillna(df['salary_inr'].mean(), inplace=True)
df['performance_rating'].fillna(df['performance_rating'].median(), inplace=True)
df['age'].fillna(df['age'].mean(), inplace=True)
df['experience_years'].fillna(df['experience_years'].mean(), inplace=True)


#  CATEGORICAL DATA CLEANING

#Fill missing 'department' with its mode (most common department)
if df['department'].isnull().sum() > 0:
    df['department'].fillna(df['department'].mode()[0], inplace=True)

# Fill missing 'city' with its mode (most common city)
if df['city'].isnull().sum() > 0:
    df['city'].fillna(df['city'].mode()[0], inplace=True)

# Replace infinity values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill any remaining NaN with column mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Replace negative salaries with mean
df['salary_inr'] = np.where(df['salary_inr'] < 0, df['salary_inr'].mean(), df['salary_inr'])


#  OUTLIER HANDLING

salary_mean = df['salary_inr'].mean()
salary_std = df['salary_inr'].std()

lower_bound = salary_mean - 3 * salary_std
upper_bound = salary_mean + 3 * salary_std

# ✅ Keep only valid salary rows
df = df[(df['salary_inr'] >= lower_bound) & (df['salary_inr'] <= upper_bound)]


#  SAVE TO EXCEL FILE

df.to_excel('cleaned_data.xlsx', index=False)

print("\n✅ Data cleaning completed successfully!")
print("➡️ Cleaned Excel file saved as 'cleaned_data.xlsx'")
print("\nMissing values after cleaning:\n")
print(df.isnull().sum())
