import pandas as pd
from os import listdir

class ETL:
    def find_xlsx_filenames(path_to_dir, suffix=".xlsx" ):
        filenames = listdir(path_to_dir)
        return [filename for filename in filenames if filename.endswith( suffix )]

    def extract(file_name: str):
        df = pd.read_excel(file_name)
        return df

    def select_cols(df):
        cols = ['Model Year', 'Mfr Name', 'Division', 'Carline', 
                'Eng Displ', '# Cyl', 'Transmission', 'City FE (Guide) - Conventional Fuel', 
                'Hwy FE (Guide) - Conventional Fuel', 'Comb FE (Guide) - Conventional Fuel', 
                'Air Aspiration Method Desc', 'Trans Desc', '# Gears', 'Drive Desc', 
                'Carline Class Desc', 'Release Date', 'City CO2 Rounded Adjusted', 
                'Hwy CO2 Rounded Adjusted', 'Comb CO2 Rounded Adjusted (as shown on FE Label)']
        
        return df[cols]
    
    def change_cases(df):
        df.loc[df["Mfr Name"] == "aston martin", "Mfr Name"] = df["Mfr Name"].str.title()
        return df

    def rename(dataframe):
        dataframe.rename(
            columns={'Eng Displ': 'Engine Displacement', '# Cyl': '# Cylinders', 'City FE (Guide) - Conventional Fuel': 'City FE', 
                    'Hwy FE (Guide) - Conventional Fuel': 'Highway FE', 'Comb FE (Guide) - Conventional Fuel': 'Combined FE',
                    'Air Aspiration Method Desc': 'Air Aspiration Method', 'Trans Desc': 'Transmission Description', 
                    'City CO2 Rounded Adjusted': 'City CO2', 'Hwy CO2 Rounded Adjusted': 'Highway CO2',
                    'Comb CO2 Rounded Adjusted (as shown on FE Label)': 'Combined CO2'},
            inplace=True,
        )
        return dataframe

    def load(targetfile, data_to_load):
        data_to_load.to_csv(targetfile, index=False)
        