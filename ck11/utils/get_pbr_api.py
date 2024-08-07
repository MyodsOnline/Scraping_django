import csv
from datetime import datetime, timedelta
import os
from typing import Tuple, Any

from dotenv import load_dotenv
import requests
import json
from django.conf import settings

from ..api_ck11.get_token_ck import get_token_ck11

load_dotenv()


def get_local_uid_list() -> list:
    """
    Запрос списка uid из csv файла, если не создана база данных
    :return: список требуемых uid для формирования запроса в api СК11
    """
    uid_list = []
    local_file_path = os.path.join(settings.BASE_DIR, 'ck11/source/pbr.csv')
    with open(local_file_path, encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) > 1:
                uid_list.append(row[1])
    return uid_list


def get_pbr_get_table_ck11(date: str, data: list) -> tuple[list, str]:
    """
    Осуществлеет запрос к api СК11 для получения данных по заданным дате и uid
    :param date: строка с датой на которую осуществляется запрос
    :param data: список uid для запроса параметров
    :return: json-подобный список словарей [{uid:"", value:[...]}, ...]
    """
    # блок преобразования даты в заданный формат
    date_end_obj = datetime.strptime(date, '%Y-%m-%d')
    date_end = date_end_obj.strftime('%Y-%m-%d')
    date_start_obj = date_end_obj - timedelta(days=1)
    date_start = date_start_obj.strftime('%Y-%m-%d')

    # блок получения данных от api СК11
    try:
        headers = get_token_ck11()
        body = {"uids": data,
                "fromTimeStamp": f"{date_start}T22:00:00Z",
                "toTimeStamp": f"{date_end}T21:00:00Z",
                "stepUnits": "seconds",
                "stepValue": 3600,
                "calculatedTimeStamp": False,
                "nullifyFutureByChangeValues": False}

        response_url = os.getenv('API_REQUEST_PATH')
        response = requests.post(response_url, headers=headers, data=json.dumps(body), verify=False)
        data_list = json.loads(response.content)['value']
        description = 'Данные от API'

    # если нет доступа к api СК11 данные забираем из локального json файла (для отладки и тестирования)
    except requests.exceptions.RequestException as e:
        print(f'This exception: {e}')
        description = 'Тестовые данные из json'

        local_file_path = os.path.join(settings.BASE_DIR, 'ck11/source/testdata.json')
        with open(local_file_path, 'r', encoding='utf-8') as jsonfile:
            data_list = json.load(jsonfile)

    return data_list, description
