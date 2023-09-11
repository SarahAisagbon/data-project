import pandas as pd

def extract(file_name):
    df = pd.read_excel(file_name)
    return df

def select_cols(dataframe):
    cols = ['Model Year', 'Mfr Name', 'Division', 'Carline', 
            'Eng Displ', '# Cyl', 'Transmission', 'City FE (Guide) - Conventional Fuel', 
            'Hwy FE (Guide) - Conventional Fuel', 'Comb FE (Guide) - Conventional Fuel', 
            'Air Aspiration Method Desc', 'Trans Desc', '# Gears', 'Drive Desc', 
            'Carline Class Desc', 'Release Date', 'City CO2 Rounded Adjusted', 
            'Hwy CO2 Rounded Adjusted', 'Comb CO2 Rounded Adjusted (as shown on FE Label)']
    return dataframe[cols]

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
    data_to_load.to_excel(targetfile)
    
if __name__ == '_main_':
    file = '2016 FEGuide for DOE-OK to release-no-sales-5-8-2019_Mercedes_public.xlsx'
    car_df = extract(file)
    print(car_df.head())
    new_car_df = select_cols(car_df)
    new_car_df = rename(new_car_df)
    load("2016 - Dataset", new_car_df)