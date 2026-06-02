import pandas as pd
import os

data_path = "data/raw"

for file in os.listdir(data_path):
    if file.endswith(".csv"):
        file_path = os.path.join(data_path, file)

        try:
            df = pd.read_csv(file_path)

            print("\n" + "=" * 60)
            print(f"FILE: {file}")
            print("=" * 60)

            print("Shape:")
            print(df.shape)

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nData Types:")
            print(df.dtypes)

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file}: {e}")

