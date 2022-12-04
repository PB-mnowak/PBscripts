import os
import re
from time import strptime
from pathlib import Path

FILE_PATH = Path(r'D:\MultiskanSky_1530-00554C')
TARGET_PATH = Path(os.getcwd())


def transfer(source_path, target_path=TARGET_PATH):
    """_summary_

    Args:
        source_path (_type_): _description_
        target_path (_type_, optional): _description_. Defaults to TARGET_PATH.
    """
    try:
        files = [file for file in os.listdir(source_path) if file.endswith('.xlsx')]
        files.sort(key=lambda x: _get_date(x), reverse=True)
        
        file_n = int(input('Number of files to transfer: '))
        open_file = input('Open transferred file? (Y/N) ').upper()

        for i in range(file_n):
            os.system(f'move "{os.path.join(source_path, files[i])}" "{target_path}" > nul')
            print(f'File: {files[i]}')
            if open_file == "Y":
                os.system(f'start excel.exe "{files[i]}" > nul')

    except WindowsError:
        print('---< ! Pendrive not detected ! >---'.center(80))
    except ValueError:
        print('---< ! Wrong value input ! >---'.center(80))
    except Exception as e:
        print(e)


def _get_date(file_name: str):
    """_summary_

    Args:
        file_name (str): _description_

    Returns:
        _type_: _description_
    """
    date_pattern = r'\d+-\d+-\d+ \d+-\d+-\d+'
    match = re.search(date_pattern, file_name)

    date_format = r'%Y-%m-%d %H-%M-%S'
    return strptime(str(match.group(0)), date_format)


if __name__ == '__main__':
    transfer(FILE_PATH)
