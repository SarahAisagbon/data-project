from automobile import ETL

def ETL_process(filenames, x):
    for file in filenames:
        year = next(x)
        car_df = ETL.extract(file)
        new_car_df = ETL.select_cols(car_df)
        new_car_df = ETL.rename(new_car_df)
        ETL.load(f"{year} - Dataset.csv", new_car_df)
    
if __file__ == " main":
    filenames = ETL.find_xlsx_filenames("/Users/sarahaisagbon/data-project")
    new_files = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
    x = (file for file in new_files)
    ETL_process(filenames, x)