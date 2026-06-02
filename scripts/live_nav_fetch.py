import requests
import pandas as pd
import os

schemes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"{fund_name}.csv"

        nav_df.to_csv(
            os.path.join(output_folder, filename),
            index=False
        )

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error fetching {fund_name}: {e}")