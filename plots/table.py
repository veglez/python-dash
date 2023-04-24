import pandas as pd
from dash import dash_table

def Table(): 
    file_path = './AIDB.csv'
    df = pd.read_csv(file_path)

    return dash_table.DataTable(data=df.to_dict('records'), page_size=10)