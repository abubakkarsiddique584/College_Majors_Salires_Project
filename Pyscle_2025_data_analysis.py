import pandas as pd

# Load the CSV file
df = pd.read_csv("payscale_data_clean.csv")

# Function to extract numeric values correctly from the format
def extract_numeric(value):
    """ Extracts numeric values from strings like 'Early Career Pay:$98,100' or 'Mid-Career Pay:$212,100' """
    if isinstance(value, str):
        value = value.split(":")[-1]  # Take the part after the last colon
        value = value.replace("$", "").replace(",", "").strip()  # Remove $ and commas
        return float(value) if value.replace(".", "").isdigit() else None  # Convert to float if numeric
    return None

# Apply extraction function to correct columns
df["Mid-Career Pay"] = df["Mid-Career Pay"].apply(extract_numeric)
df["% High Meaning"] = df["% High Meaning"].apply(extract_numeric)

# Drop any rows with missing values after cleaning
df.dropna(inplace=True)

# Find max values in each column
max_mid_career = df.loc[df["Mid-Career Pay"].idxmax()]
max_high_meaning = df.loc[df["% High Meaning"].idxmax()]

# Display the results
print("\n🎯 Major with the Highest Mid-Career Pay:")
print(max_mid_career)

print("\n🎯 Major with the Highest % High Meaning:")
print(max_high_meaning)

# ------------------- SECOND CODE -------------------

# Function to clean up column values
def clean_value(value):
    """Extract numeric values and remove unnecessary prefixes."""
    if isinstance(value, str):
        value = value.split(":")[-1].strip()  # Remove column name prefix like 'Rank:', 'Mid-Career Pay:', etc.
        value = value.replace("$", "").replace(",", "").strip()  # Remove dollar signs and commas
        return float(value) if value.replace(".", "").isdigit() else value  # Convert numbers to float
    return value

# Apply cleanup to all columns
df = df.apply(lambda col: col.map(clean_value) if col.dtype == "object" else col)

# Rename columns to remove prefixes
df.columns = ["Rank", "Major", "Degree Type", "Early Career Pay", "Mid-Career Pay", "% High Meaning"]

# Convert necessary columns to numeric values
df["Mid-Career Pay"] = pd.to_numeric(df["Mid-Career Pay"], errors='coerce')
df["% High Meaning"] = pd.to_numeric(df["% High Meaning"], errors='coerce')

# Drop any rows with missing values after conversion
df.dropna(inplace=True)

# Calculate salary growth
df["Salary Increase"] = df["% High Meaning"] - df["Mid-Career Pay"]

# Get the top 5 degrees with the highest salary increase
top_5_growth = df.nlargest(5, "Salary Increase")

# Display the results in a readable format
print("\n🏆 **Top 5 Degrees with Highest Salary Growth (Mid-Career Pay to High Meaning Pay):**\n")
print(top_5_growth[["Rank", "Major", "Degree Type", "Mid-Career Pay", "% High Meaning", "Salary Increase"]].to_string(index=False))
