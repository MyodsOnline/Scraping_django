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
    Обрабатывает POST-запрос, извлекает целевую дату и время, преобразует их в нужный формат
    и ищет соответствующий файл в заданной директории.

    Info:
        - Получает дату и время из параметров POST-запроса.
        - Преобразует дату и время в строковый формат для формирования имени директории и файла.
        - Вызывает функцию `find_bars_file` для поиска файла в соответствующей директории.
        - Возвращает JSON-ответ с сообщением о результате поиска.

    Args:
        request (HttpRequest): Объект HTTP-запроса, содержащий данные POST-запроса.

    Returns:
        JsonResponse: Ответ в формате JSON с ключом 'message', содержащим результат поиска файла.
    """
    target_datetime = request.POST.get('target_datetime')
    dt = datetime.strptime(target_datetime, "%Y-%m-%dT%H:%M")

    # преобразование полученных данных в заданный формат
    directory_name = dt.strftime("%d%m%y")
    hour = int(dt.strftime("%H")) + 24
    file_name = f"smzu_mega_XML_UR_MDP_{hour}.os"

    # поиск файла в директории
    message = find_bars_file(directory_name, file_name)

    if "Возникла ошибка" in message:
        return JsonResponse({"status": "error", "message": message})
    else:
        return JsonResponse({"status": "success", "message": message})


def find_bars_file(directory_name: str, file_name: str) -> str:
    """
    Ищет указанный файл в заданной директории, проверяет его существование и копирует его в рабочую директорию.

    Args:
        directory_name (str): Имя папки, в которой следует искать файл.
        file_name (str): Имя файла, который нужно найти.

    Returns:
        str: Путь к скопированному файлу, если файл успешно найден и скопирован.
        str: Сообщение об ошибке, если директория или файл не найдены.

    Raises:
        FileNotFoundError: Возникает, если указанный каталог или файл отсутствуют.
    """
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


def copy_file_to_work_dir(file_path: str) -> str:
    """
    Копирует файл в рабочую директорию и записывает путь исходного файла в новый файл.

    Args:
    ----------
    file_path : str
        Путь к исходному файлу, который нужно скопировать.

    Returns:
    -------
    str
        Сообщение об успешном копировании файла или сообщение об ошибке.

    Raises:
    ------
    FileNotFoundError
        Если указанный файл не найден.
    PermissionError
        Если у программы нет прав доступа к файлу или директории.
    """
    destination_file_name = "work_file"
    destination_file_path = os.path.join(WORKDIR_PATH, destination_file_name)

    try:
        shutil.copyfile(file_path, destination_file_path)

        with open(destination_file_path, 'w', encoding='utf-8') as file:
            file.write(file_path)

        return f'Файл "{file_path.split("/Bars_files/")[-1]}" скопирован в "{destination_file_path}"'

    except FileNotFoundError:
        return f"Ошибка: файл {file_path} не найден."
    except PermissionError:
        return "Ошибка: недостаточно прав для копирования файла."
    except Exception as e:
        return f"Ошибка при копировании файла: {e}"
