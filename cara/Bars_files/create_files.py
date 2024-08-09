import os


def create_data() -> None:
    """
    Функция для создания тестовых директорий и файлов
    """
    days = range(1, 31)
    files = range(25, 49)

    for day in days:
        folder_name = f"{str(day).zfill(2)}0824"
        os.makedirs(folder_name, exist_ok=True)

        for file_number in files:
            file_name = f"smzu_mega_XML_UR_MDP_{str(file_number).zfill(2)}.os"
            file_path = os.path.join(folder_name, file_name)

            with open(file_path, 'w') as file:
                pass


if __name__ == '__main__':
    create_data()
