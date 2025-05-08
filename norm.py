import pandas as pd
import os

# Script to prompt for directory and merge normalized CSV files
script_code = '''
import os
import pandas as pd

def normalize_columns(columns):
    return [col.strip().lower().replace(" ", "_") for col in columns]

def merge_csv_files(folder_path):
    all_data = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            try:
                df = pd.read_csv(file_path)
                df.columns = normalize_columns(df.columns)
                df["source_file"] = filename
                all_data.append(df)
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
    
    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        output_path = os.path.join(folder_path, "merged_output.csv")
        merged_df.to_csv(output_path, index=False)
        print(f"Successfully merged files. Output saved to: {output_path}")
    else:
        print("No valid CSV files found to merge.")

if __name__ == "__main__":
    folder = input("Enter the folder path containing CSV files to merge: ").strip()
    if os.path.isdir(folder):
        merge_csv_files(folder)
    else:
        print("Invalid folder path.")
'''

# Save this script to a file
script_path = "/mnt/data/merge_normalize_csvs.py"
with open(script_path, "w") as f:
    f.write(script_code)

script_path
