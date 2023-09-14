from ETL_operations import ETL
import pandas as pd
import os

def main():
    path = os.path.abspath(os.getcwd())
    filenames = ETL.find_filenames(path)
    filenames = sorted(filenames)
    new_files = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
    x = (file for file in new_files)
    for file in filenames:
        year = next(x)
        car_df = ETL.extract(file)
        try:
            new_car_df = ETL.select_cols(car_df)
        except:
            new_car_df = car_df
        new_car_df = ETL.change_cases(new_car_df)
        new_car_df = ETL.rename(new_car_df)
        ETL.load(f"{year} - Dataset.csv", new_car_df)
        # Try to delete the file.
        try:
            os.remove(file)
        except OSError as e:
            # If it fails, inform the user.
            print("Error: %s - %s." % (e.filename, e.strerror))

def store():
    # list all csv files only
    path = os.path.abspath(os.getcwd())
    csv_files = ETL.find_filenames(path, ".csv")
    csv_files.sort()
    print(len([pd.read_csv(file) for file in csv_files ]))
    df = pd.concat([pd.read_csv(file) for file in csv_files ], ignore_index=True)
    ETL.load("Dataset.csv", df)
    return df
      
if __name__ == '__main__':
    main()
    df_concat = store()
