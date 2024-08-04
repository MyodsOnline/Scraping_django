import csv
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import requests
import json
from django.conf import settings

from ..api_ck11.get_token_ck import get_token_ck11

load_dotenv()


def get_pbr_get_table_ck11(date: str, data=None) -> json:

    date_end_obj = datetime.strptime(date, '%Y-%m-%d')
    date_end = date_end_obj.strftime('%Y-%m-%d')
    date_start_obj = date_end_obj - timedelta(days=1)
    date_start = date_start_obj.strftime('%Y-%m-%d')

    uid_list = []
    if data:
        for el in data:
            uid_list.append(el.uid)
        print(f'List from request: {uid_list}')
    else:
        local_file_path = os.path.join(settings.BASE_DIR, 'ck11/source/pbr.csv')
        with open(local_file_path, encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) > 1:
                    uid_list.append(row[1])
        print(f'List from file: {uid_list}')

    try:
        headers = get_token_ck11()
        body = {"uids": uid_list,
                "fromTimeStamp": f"{date_start}T22:00:00Z",
                "toTimeStamp": f"{date_end}T21:00:00Z",
                "stepUnits": "seconds",
                "stepValue": 3600,
                "calculatedTimeStamp": False,
                "nullifyFutureByChangeValues": False}

        response_url = os.getenv('API_REQUEST_PATH')
        response = requests.post(response_url, headers=headers, data=json.dumps(body), verify=False)
        data_list = json.loads(response.content)['value']

    except requests.exceptions.RequestException as e:
        print(f'This exception: {e}')
        local_file_path = os.path.join(settings.BASE_DIR, 'ck11/source/testdata.json')
        with open(local_file_path, 'r', encoding='utf-8') as jsonfile:
            data_list = json.load(jsonfile)

    return data_list


if __name__ == '__main__':
    get_pbr_get_table_ck11('2024-07-02')
