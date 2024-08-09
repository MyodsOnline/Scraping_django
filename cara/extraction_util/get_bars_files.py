import os
import shutil

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
def test_func(request):
    """
    Функция получает дату и время из fetch-запроса
    """
    date = request.POST.get('date-input')
    time = request.POST.get('time-input')

    # преобразование полученных данных в заданный формат
    directory_name = date[8:] + date[5:7] + date[2:4]
    hour = int(time[:2]) + 25
    file_name = f"smzu_mega_XML_UR_MDP_{hour}.os"

    # формируем тестовую строку ответа
    message = f"Дата {directory_name} файл {file_name}"

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
        return f'Error: {e}'


def copy_file_to_work_dir(file_path) -> str:
    try:
        destination_file_path = os.path.join(WORKDIR_PATH, "bars_file.os")
        shutil.copyfile(file_path, destination_file_path)
        return f'Файл {file_path} скопирован в "{WORKDIR_PATH}"'
    except Exception as e:
        return f"Ошибка при копировании файла: {e}"
