import os
import json
import pandas as pd


file_path = os.path.join(os.getcwd(), 'response.json')
abs_path = f'/Users/diver.vlz/Documents/django_projects/Scraping_django/Scraping_srver/ck11/source/response.json'

print(file_path)
print(abs_path)
print(file_path == abs_path)

with open(abs_path, encoding='utf-8-sig') as f:
    data = json.load(f)
    data_frame = pd.read_json(f)
    print(data_frame)
