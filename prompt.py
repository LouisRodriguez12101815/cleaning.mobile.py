import re

# Define file paths for each of the uploaded CSV files
file_paths = [
    '/mnt/data/27-03-2024 moeabbas856@gmail.com-2024-03-26 CHERRY SMS - AG 03-26.csv',
    '/mnt/data/28-03-2024 moeabbas856@gmail.com-2024-03-27 CHERRY SMS - NEWBLAST 12-20-23.csv',
    '/mnt/data/26-03-2024 moeabbas856@gmail.com-2024-03-25 APP LEAD LIST - blast 1.csv',
    '/mnt/data/26-03-2024 moeabbas856@gmail.com-2024-03-25 APP LEAD LIST - BLAST CONSULTING.csv',
    '/mnt/data/26-03-2024 moeabbas856@gmail.com-2024-03-25 CHERRY SMS - AG 03-25 (1).csv',
    '/mnt/data/27-03-2024 moeabbas856@gmail.com-2024-03-26 APP LEAD LIST - blast 2.csv'
]

# Function to extract phone numbers from a dataframe
def extract_phone_numbers(data):
    phone_numbers = []
    # Compile a regular expression for phone numbers
    phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')

    # Search each column for phone numbers
    for column in data.columns:
        matches = data[column].astype(str).str.extractall(phone_pattern)
        if not matches.empty:
            phone_numbers.extend(matches[0].unique().tolist())

    return phone_numbers

# Load each file, extract phone numbers, and combine them into a single list
all_phone_numbers = []
for path in file_paths:
    try:
        df = pd.read_csv(path, error_bad_lines=False)
        phone_numbers = extract_phone_numbers(df)
        all_phone_numbers.extend(phone_numbers)
    except Exception as e:
        print(f"Error processing file {path}: {e}")

# Deduplicate the list of phone numbers
unique_phone_numbers = list(set(all_phone_numbers))

# Display the list of unique phone numbers
unique_phone_numbers
