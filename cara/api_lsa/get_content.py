import os

from get_access import get_tokens, get_svg


def get_svg_content() -> str:
    """
    Функция возвращает svg со схемой при успешной аутентификации или пустую строку

    :returns: строка, содержащая svg файйл
    """
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    try:
        access_token, _ = get_tokens(login, password)
        svg_content = get_svg(access_token)
    except Exception as e:
        print(f"error - {e}")
        svg_content = ""
    return svg_content
