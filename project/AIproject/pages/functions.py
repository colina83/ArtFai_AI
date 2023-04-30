import pandas as pd
import numpy as np
import requests
import os


def create_url(search):
    key = "38e8628b-5bf1-40c0-85dd-72c788315a1b"
    url = f'https://api.harvardartmuseums.org/object?person={search}&apikey={key}'
    return url

def results_provenance(url, df=pd.DataFrame()):
    r = requests.get(url)
    data = r.json()
    info = data['info']
    records = data['records']
    
    # Extract relevant data from each record
    record_data = []
    for record in records:
        record_data.append({
            'title': record['title'],
            'classification': record['classification'],
            'century': record['century'],
            'provenance': record['provenance']
        })
    
    # Append record data to DataFrame
    df = pd.concat([df, pd.DataFrame(record_data)], ignore_index=True)
    
    # Recursively call pagination function for next page, if it exists
    if 'next' in info:        
        return results_provenance(info['next'], df)
    else:
        return df
