from ETL_operations import ETL
import pandas as pd
import os

def main():
    path = os.path.abspath('raw_data') 
    filenames = ETL.find_filenames(path)
    filenames = sorted(filenames)
    new_files = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
    x = (file for file in new_files)
    for file in filenames:
        try:
            path = os.path.abspath('raw_data') + '/' + file
        except:
            path = os.path.abspath('raw_data') + "\\" + file
        year = next(x)
        car_df = ETL.extract(path)
        try:
            new_car_df = ETL.select_cols(car_df)
        except:
            new_car_df = car_df
        new_car_df = ETL.change_cases(new_car_df)
        new_car_df = ETL.wrap(new_car_df)
        new_car_df = ETL.rename(new_car_df)
        try:
            path = os.path.abspath('clean_data') + '/' + f"{year} - Dataset.csv"
        except:
            path = os.path.abspath('clean_data') + '\\' + f"{year} - Dataset.csv"
        ETL.load(path, new_car_df)
        
def store():
    # list all csv files only
    path = os.path.abspath('clean_data')    
    csv_files = ETL.find_filenames(path, ".csv")
    csv_files.sort()
    fulldf = []
    for file in csv_files:
        try:
            fulldf.append(pd.read_csv(path + '/' + file))
        except:
            fulldf.append(pd.read_csv(path + '\\' + file))
    df = pd.concat(fulldf, ignore_index=True)
    ETL.load("Dataset.csv", df)
    
if __name__ == '__main__':
    main()
    store()
