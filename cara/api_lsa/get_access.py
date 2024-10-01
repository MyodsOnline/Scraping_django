from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()


def get_tokens(login: str, password: str) -> tuple:
    """
    Функция получения токенов аутентификации на сервере svg-схемы
    """
    svg_api_url = os.getenv("SVG_API_URL")
    data = {"login": login, "password": password}
    headers = {"Content-Type": "application/json"}
    response = requests.post(svg_api_url, data=json.dumps(data), headers=headers, verify=False)

    if response.status_code == 200:
        tokens = response.json()
        return tokens["access_token"], tokens["refresh_token"]
    else:
        raise Exception("Failed to authenticate")


def get_svg(access_token: str) -> str:
    """
    Функция получения svg-схемы с сервера по токену аутентификации
    """
    svg_url = os.getenv("SVG_URL")
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(svg_url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to load SVG")
