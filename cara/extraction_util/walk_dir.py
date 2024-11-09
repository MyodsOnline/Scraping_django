import os
import shutil
from datetime import datetime

from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from typing import List, Optional
import py7zr

TEST = True

if TEST:
    # пути к тестовым файлам расчета
    CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
    BASE_PATH = os.path.join(CURRENT_DIR, 'Good')
    WORKDIR_PATH = os.path.join(CURRENT_DIR, 'Work_dir')

else:
    BASE_PATH = r"\\srv-smzu2-sz\CFRAS\FilesRegim\Good"


def get_current_datetime() -> datetime:
    """
    Возвращает текущую дату и время.

    Returns:
        datetime: Текущая дата и время.
    """
    return datetime.now()


def get_sorted_date_dirs(base_path: str) -> List[str]:
    """
    Возвращает список директорий с датами, отсортированный в порядке убывания.

    Args:
        base_path (str): Путь к каталогу, в котором нужно искать папки с датами.

    Returns:
        List[str]: Список папок с датами, отсортированный от самой новой к самой старой.
    """
    date_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    return sorted(date_dirs, reverse=True)


def find_closest_date_dir(date_dirs: List[str], current_datetime: datetime) -> Optional[str]:
    """
    Находит ближайшую папку с датой, которая не превышает текущую дату.

    Args:
        date_dirs (List[str]): Список названий папок с датами.
        current_datetime (datetime): Текущая дата и время для сравнения.

    Returns:
        Optional[str]: Название ближайшей папки с датой или None, если ничего не найдено.
    """
    for date_dir in date_dirs:
        try:
            date_obj = datetime.strptime(date_dir, '%Y_%m_%d')
            if date_obj <= current_datetime:
                return date_dir
        except ValueError:
            continue
    return None


def find_closest_time_dir(date_dir: str, base_path: str, current_datetime: datetime) -> Optional[str]:
    """
    Находит ближайшую папку со временем в указанной папке с датой.

    Args:
        date_dir (str): Название папки с датой.
        base_path (str): Базовый путь к каталогу с папкой даты.
        current_datetime (datetime): Текущая дата и время для сравнения.

    Returns:
        Optional[str]: Название ближайшей папки со временем или None, если ничего не найдено.
    """
    time_dir_path = os.path.join(base_path, date_dir)
    time_dirs = [d for d in os.listdir(time_dir_path) if os.path.isdir(os.path.join(time_dir_path, d))]
    closest_time_dir = None
    min_time_diff = None

    for time_dir in time_dirs:
        try:
            time_obj = datetime.strptime(time_dir, '%H_%M_%S').time()
            full_time = datetime.combine(datetime.strptime(date_dir, '%Y_%m_%d').date(), time_obj)
            time_diff = abs((full_time - current_datetime).total_seconds())

            if min_time_diff is None or time_diff < min_time_diff:
                min_time_diff = time_diff
                closest_time_dir = time_dir
        except ValueError:
            continue
    return closest_time_dir


def copy_file_to_workdir(source_file_path: str, destination_file_path: str) -> None:
    """
    Копирует указанный файл в рабочую директорию с новым именем.

    Args:
        source_file_path (str): Путь к исходному файлу.
        destination_file_path (str): Путь к файлу в рабочей директории.

    Raises:
        FileNotFoundError: Если исходный файл не найден.
    """
    if not os.path.isfile(source_file_path):
        raise FileNotFoundError(f"Файл mdp_debug_0 не найден в {source_file_path}")
    shutil.copy2(source_file_path, destination_file_path)


def get_SMZU_file() -> str:
    """
    Создает копию файла 'mdp_debug_0' в рабочей директории и возвращает строку с датой и временем.

    Returns:
        str: Строка в формате 'YYYY-MM-DDTHH:MM' для использования в HTML-шаблоне.

    Raises:
        Exception: Если не найдена подходящая папка с датой или временем.
    """
    current_datetime = get_current_datetime()
    date_dirs = get_sorted_date_dirs(BASE_PATH)

    closest_date_dir = find_closest_date_dir(date_dirs, current_datetime)
    if not closest_date_dir:
        raise Exception("Нет подходящей папки с датой")

    closest_time_dir = find_closest_time_dir(closest_date_dir, BASE_PATH, current_datetime)
    if not closest_time_dir:
        raise Exception("Нет подходящей папки со временем")

    source_file_path = os.path.join(BASE_PATH, closest_date_dir, closest_time_dir, 'mdp_debug_0')
    destination_file_path = os.path.join(WORKDIR_PATH, 'work_file')
    copy_file_to_workdir(source_file_path, destination_file_path)

    date_part = closest_date_dir.replace('_', '-')
    time_part = closest_time_dir[:5].replace('_', ':')
    result_str = f"{date_part}T{time_part}"

    return result_str


def scan_basedir() -> list:
    """
    Функция возвращает список папок по заданному пути.

    Raises:
        FileNotFoundError: файл не найден
        PermissionError: доступ запрещен
    Returns:
        - список папок внутри директории или сообщение об ошибке, если путь не найден
    """
    try:
        first_level_dirs = []
        with os.scandir(BASE_PATH) as base_dir:
            for sub_directory in base_dir:
                if sub_directory.is_dir():
                    first_level_dirs.append(sub_directory.name)
        return first_level_dirs
    except FileNotFoundError:
        return ['Нет файлов']
    except PermissionError:
        return ['Доступ закрыт']


@require_POST
@csrf_exempt
def get_fetch_response(request: HttpRequest) -> JsonResponse:
    """
    Обрабатывает POST-запрос, извлекает дату и время,
    вызывает функцию сканирования поддиректорий и возвращает JSON-ответ с сообщением.

    Args:
        request (HttpRequest): Объект запроса, содержащий данные POST.
    Returns:
        JsonResponse: Ответ с сообщением в формате JSON.
    """
    date = request.POST.get('date-input')
    time = request.POST.get('time-input').replace(':', '_')
    message = scan_subdirectories(date, time)
    return JsonResponse({'message': message})


def scan_subdirectories(directory_name: str, file_name: str) -> str:
    """
    Ищет директорию по указанному пути
    Выбранное пользователем дата и время в вормате строки

    Args:
        directory_name: Путь к директории для сканирования.
        file_name: Префикс, с которого должно начинаться название поддиректории.
    Returns:
        Название поддиректории, если она найдена; иначе сообщение о том, что поддиректория не найдена.
    """
    subdir_path = os.path.join(BASE_PATH, directory_name)
    if os.path.isdir(subdir_path):
        with os.scandir(subdir_path) as directory:
            for entry in directory:
                if entry.name.startswith(file_name):
                    file_path = os.path.join(subdir_path, entry.name)
                    check_path(file_path)
                    return f'Файл режима за ' \
                           f'{directory_name.replace("_", ".")} ' \
                           f'{entry.name.split(".")[0].replace("_", ":")}'
        return f'Расчета за время {file_name.replace("_", ".")} нет в базе'
    else:
        return f'Директории {directory_name} нет в папке {BASE_PATH}'


def check_path(file_path: str) -> None:
    """
    Проверяет, является ли путь директорией или архивом, и копирует либо извлекает содержимое в рабочую директорию.

    Args:
        file_path (str): Путь к директории или архиву.

    Returns:
        None
    """
    clear_directory()
    if os.path.isdir(file_path):
        shutil.copytree(file_path, os.path.join(WORKDIR_PATH, os.path.basename(file_path)))
    else:
        extract_archive(file_path)


def extract_archive(archive_path: str) -> None:
    """
    Извлекает содержимое 7z архива в рабочую директорию.

    Args:
        archive_path (str): Путь к 7z архиву.

    Returns:
        None
    """
    with py7zr.SevenZipFile(archive_path, 'r') as archive:
        archive.extractall(path=WORKDIR_PATH)


def clear_directory() -> None:
    """
    Удаляет все файлы и папки в рабочей директории.

    Returns:
        None
    """
    for filename in os.listdir(WORKDIR_PATH):
        file_path = os.path.join(WORKDIR_PATH, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    print(f"Directory '{WORKDIR_PATH}' cleared.")


if __name__ == '__main__':
    get_SMZU_file()
