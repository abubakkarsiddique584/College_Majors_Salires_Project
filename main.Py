import pandas as pd

# Load Data
df = pd.read_csv('salaries_by_college_majors.csv')

# Drop missing values
clean_df = df.dropna().copy()  # Prevent SettingWithCopyWarning

# Ensure column names are stripped of any extra spaces
clean_df.columns = clean_df.columns.str.strip()

# Debugging: Check column names
print("Column Names:", clean_df.columns)

# Highest Starting Median Salary
if not clean_df.empty:
    highest_starting_pay = clean_df['Starting Median Salary'].idxmax()
    highest_starting_major = clean_df.loc[highest_starting_pay, 'Undergraduate Major']
    highest_starting_salary = clean_df.loc[highest_starting_pay, 'Starting Median Salary']

    print(f"\n📌 Highest Starting Salary Major: {highest_starting_major} - ${highest_starting_salary:,.2f}")

# Highest Mid-Career Median Salary
if not clean_df.empty:
    highest_mid_career_pay = clean_df['Mid-Career Median Salary'].idxmax()
    highest_mid_career_major = clean_df.loc[highest_mid_career_pay, 'Undergraduate Major']
    highest_mid_career_salary = clean_df.loc[highest_mid_career_pay, 'Mid-Career Median Salary']

    print(f"📌 Highest Mid-Career Salary Major: {highest_mid_career_major} - ${highest_mid_career_salary:,.2f}")

# Lowest Starting Salary
if not clean_df.empty:
    lowest_starting_pay = clean_df['Starting Median Salary'].idxmin()
    lowest_starting_major = clean_df.loc[lowest_starting_pay, 'Undergraduate Major']
    lowest_starting_salary = clean_df.loc[lowest_starting_pay, 'Starting Median Salary']

    print(f"📌 Lowest Starting Salary Major: {lowest_starting_major} - ${lowest_starting_salary:,.2f}")

# Create 'Spread' column (Difference between 90th and 10th percentile salaries)
if 'Mid-Career 90th Percentile Salary' in clean_df.columns and 'Mid-Career 10th Percentile Salary' in clean_df.columns:
    clean_df['Spread'] = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

# Find the Major with the Highest Spread
if not clean_df.empty:
    highest_spread_idx = clean_df['Spread'].idxmax()
    highest_spread_major = clean_df.loc[highest_spread_idx, 'Undergraduate Major']
    highest_spread_value = clean_df.loc[highest_spread_idx, 'Spread']

    print(f"📌 Major with Highest Salary Spread: {highest_spread_major} - ${highest_spread_value:,.2f}")

# Low Risk Majors (Sorted by Lowest Salary Spread)
low_risk = clean_df.sort_values('Spread', ascending=True).reset_index(drop=True)
print("\n📉 Lowest Salary Spread Majors:")
print(low_risk[['Undergraduate Major', 'Spread']].head())

# Top 5 Degrees by **Highest 90th Percentile Salary**
top_5_degrees_90th = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False).reset_index(drop=True)
print("\n🏆 Top 5 Majors with Highest 90th Percentile Salary:")
print(top_5_degrees_90th[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

# 🔥 **Top 5 Degrees by Mid-Career Median Salary**
top_5_mid_career = clean_df.sort_values('Mid-Career Median Salary', ascending=False).reset_index(drop=True)
print("\n💼 Top 5 Majors by Mid-Career Median Salary:")
print(top_5_mid_career[['Undergraduate Major', 'Mid-Career Median Salary']].head())

# Group by 'Group' and compute the mean for numeric columns only
if 'Group' in clean_df.columns:
    group_mean_summary = clean_df.groupby('Group').mean(numeric_only=True)
    print("\n📊 Group-Wise Salary Statistics:")
    print(group_mean_summary)

# Majors with Largest Salary Spread
largest_spread = clean_df.sort_values('Spread', ascending=False).reset_index(drop=True)
print("\n💰 Majors with Largest Salary Spread:")
print(largest_spread[['Undergraduate Major', 'Spread']].head())

# Majors with Lowest Salary Spread
lowest_spread = clean_df.sort_values('Spread', ascending=True).reset_index(drop=True)
print("\n📉 Majors with Lowest Salary Spread:")
print(lowest_spread[['Undergraduate Major', 'Spread']].head())
