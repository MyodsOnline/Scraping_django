import os
from django.conf import settings


def return_svg_from_file(path: str) -> str:
    base_path = os.path.join(settings.BASE_DIR, f'ck11/source/{path}')
    with open(base_path, encoding='utf-8') as svg_file:
        svg_string = svg_file.read()
    return svg_string


if __name__ == '__main__':
    print(return_svg_from_file('output.svg'))
