import os
from django.conf import settings


def return_svg_from_file(path: str) -> str:
    """
        Читает SVG-файл с заданного пути и возвращает его содержимое в виде строки.

        Args:
            path (str): Относительный путь к SVG-файлу от корневой директории проекта.

        Returns:
            str: Строка, содержащая содержимое SVG-файла.

        Raises:
            - FileNotFoundError: Может возникнуть, если файл не существует по указанному пути.
            - IOError: Может возникнуть при проблемах с чтением файла.
            - UnicodeDecodeError: Может возникнуть, если файл не может быть декодирован с помощью UTF-8.
        """
    try:
        base_path = os.path.join(settings.BASE_DIR, f'ck11/source/{path}')
        with open(base_path, encoding='utf-8') as svg_file:
            svg_string = svg_file.read()
        return svg_string
    except FileNotFoundError:
        return f"Ошибка: Файл по пути '{path}' не найден."
    except IOError:
        return f"Ошибка: Не удалось прочитать файл по пути '{path}'."
    except UnicodeDecodeError:
        return f"Ошибка: Файл по пути '{path}' не может быть декодирован с использованием UTF-8."


if __name__ == '__main__':
    print(return_svg_from_file('output.svg'))
