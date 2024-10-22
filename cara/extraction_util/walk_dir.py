import os
import shutil
from datetime import datetime

from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import py7zr

TEST = True

if TEST:
    # пути к тестовым файлам расчета
    CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
    BASE_PATH = os.path.join(CURRENT_DIR, 'Good')
    WORKDIR_PATH = os.path.join(CURRENT_DIR, 'Work_dir')

else:
    BASE_PATH = r"\\srv-smzu2-sz\CFRAS\FilesRegim\Good"


def get_SMZU_file() -> str:
    """
    Функция создает копию файла mdp_debug_0 в WORKDIR_PATH
    :return: строка формата YYYY-MM-DDTHH:MM для использования в html шаблоне
    """

    # получаем текущую дату и время для поиска ближайшего файла расчета
    current_datetime = datetime.now()

    # сканируем родительский каталог для поиска папки с датой, ближайшей к текущей
    date_dirs = [d for d in os.listdir(BASE_PATH) if os.path.isdir(os.path.join(BASE_PATH, d))]
    date_dirs = sorted(date_dirs, reverse=True)
    closest_date_dir = None

    for date_dir in date_dirs:
        try:
            date_obj = datetime.strptime(date_dir, '%Y_%m_%d')
            if date_obj <= current_datetime:
                closest_date_dir = date_dir
                break
        except ValueError:
            continue

    # продумать вариант с базовым шаблоном, чтобы не крашить программу
    if not closest_date_dir:
        raise Exception("Нет подходящей папки с датой")

    # сканируем полученную ранее директорию для поиска последней по времени папки
    time_dir_path = os.path.join(BASE_PATH, closest_date_dir)
    time_dirs = [d for d in os.listdir(time_dir_path) if os.path.isdir(os.path.join(time_dir_path, d))]
    closest_time_dir = None
    min_time_diff = None

    for time_dir in time_dirs:
        try:
            time_obj = datetime.strptime(time_dir, '%H_%M_%S').time()
            full_time = datetime.combine(datetime.strptime(closest_date_dir, '%Y_%m_%d').date(), time_obj)
            time_diff = abs((full_time - current_datetime).total_seconds())

            if min_time_diff is None or time_diff < min_time_diff:
                min_time_diff = time_diff
                closest_time_dir = time_dir
        except ValueError:
            continue

    if not closest_time_dir:
        raise Exception("Нет подходящей папки со временем")

    # копируем искомый файл в заданный путь, меняем название на work_file
    source_file_path = os.path.join(time_dir_path, closest_time_dir, 'mdp_debug_0')
    if not os.path.isfile(source_file_path):
        raise FileNotFoundError(f"Файл mdp_debug_0 не найден в {source_file_path}")

    destination_file_path = os.path.join(WORKDIR_PATH, 'work_file')
    shutil.copy2(source_file_path, destination_file_path)

    # получаем строку для использования в html шаблоне
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
    Функция копирует или извлекает содержимое архива в рабочую директорию
    :param file_path: путь к директории или архиву
    :return: None
    """
    clear_directory()
    if os.path.isdir(file_path):
        shutil.copytree(file_path, os.path.join(WORKDIR_PATH, os.path.basename(file_path)))
    else:
        extract_archive(file_path)


def extract_archive(archive_path: str) -> None:
    """
    Функция извлекает архив в заданную директорию.
    :param archive_path: путь к 7z архиву
    :return: None
    """
    with py7zr.SevenZipFile(archive_path, 'r') as archive:
        archive.extractall(path=WORKDIR_PATH)


def clear_directory() -> None:
    """
    Функция производит удаление всех дирекорий и файлов по заданному пути.
    :param extract_path: путь к директории
    :return: None
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
