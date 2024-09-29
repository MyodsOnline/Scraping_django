import os
import shutil
from datetime import datetime

from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

TEST = True
if TEST:
    # пути к тестовым файлам расчета
    CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
    BASE_PATH = os.path.join(CURRENT_DIR, 'Bars_files')
    WORKDIR_PATH = os.path.join(CURRENT_DIR, 'Work_dir')


@require_POST
@csrf_exempt
def get_target_datetime(request):
    """
    Функция получает дату и время из fetch-запроса
    """
    target_datetime = request.POST.get('target_datetime')
    dt = datetime.strptime(target_datetime, "%Y-%m-%dT%H:%M")

    # преобразование полученных данных в заданный формат
    directory_name = dt.strftime("%d%m%y")
    hour = int(dt.strftime("%H")) + 24
    file_name = f"smzu_mega_XML_UR_MDP_{hour}.os"

    # поиск файла в директории
    message = find_bars_file(directory_name, file_name)

    return JsonResponse({'message': message})


def find_bars_file(directory_name, file_name):
    try:
        target_dir = os.path.join(BASE_PATH, directory_name)
        if not os.path.exists(target_dir) or not os.path.isdir(target_dir):
            raise FileNotFoundError(f"Папка '{target_dir}' не найдена в '{BASE_PATH}'")

        file_path = os.path.join(target_dir, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл '{file_name}' не найден в папке '{target_dir}'")

        copy_file = copy_file_to_work_dir(file_path)
        return copy_file

    except FileNotFoundError as e:
        return f'Возникла ошибка: {e}'


def copy_file_to_work_dir(file_path) -> str:
    try:
        destination_file_path = os.path.join(WORKDIR_PATH, "work_file")
        shutil.copyfile(file_path, destination_file_path)
        with open(destination_file_path, 'w', encoding='utf-8') as file:
            file.write(f'{file_path}')

        return f'Файл {file_path} скопирован в "{WORKDIR_PATH}"'
    except Exception as e:
        return f"Ошибка при копировании файла: {e}"
