from os import path

import pandas as pd
from pathlib import Path

def process(path_to_data,file_prefix:str, output_file_name:str):
    cwd = Path.cwd()
    data_dir = Path(cwd/path_to_data)
    dataframes = []

    total_row_before_filter_and_concat, total_size_after_filter, concated_row_count = 0,0,0
    
    releveant_files = sorted(
        f for f in data_dir.iterdir() if f.is_file() and f.name.startswith(file_prefix)
    )

    for file in releveant_files:
        df = pd.read_csv(file)
        total_row_before_filter_and_concat += len(df)
        df = df[df['PropertyType'] == "Residential"]
        total_size_after_filter += len(df)
        dataframes.append(df)

    if dataframes:
        output_path = Path(cwd/output_file_name)
        concated_df = pd.concat(dataframes, axis=0, ignore_index=True)
        concated_row_count += len(concated_df)
        concated_df.to_csv(output_path)


    print(f"Total Row count before Filtering and Concating: {total_row_before_filter_and_concat} Rows.")
    print(f"Total Row count after Filtering : {total_size_after_filter} Rows.")
    print(f"Total Row count after Concating : {concated_row_count} Rows.")

    return total_row_before_filter_and_concat, total_size_after_filter, concated_row_count


### Concating and Filter Listing Datasets
process(r"data\csv", "CRMLSListing",r"src\week1\Combined_Residential_Listings.csv")
"""
Row Counts:
Total Row count before Filtering and Concating: 860898 Rows.
Total Row count after Filtering : 547162 Rows.
Total Row count after Concating : 547162 Rows.

"""
        
### Concating and Filter Sold Datasets
process(r"data\csv", "CRMLSSold",r"src\week1\Combined_Residential_Sold.csv")
"""
Row Counts:
Total Row count before Filtering and Concating: 615707 Rows.
Total Row count after Filtering : 414054 Rows.
Total Row count after Concating : 414054 Rows.

"""
            

