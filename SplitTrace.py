from time import time
from sys import argv
import os


class Spliter:
    files = {}

    def __init__(self, input_file):
        self.input_file_name = input_file
        self.input_file = self.open_file(self.input_file_name)
        self.files[self.input_file_name] = self.input_file


        self.readed_data_size = 0
        self.progressbar_counter = 0

    def split_files(self, mode: str):
        PROGRESSBAR_STEP = os.path.getsize(self.input_file_name) // 10
        print('[          ]  0%', end='')

        for line in self.input_file:
            if self.readed_data_size == 0:  # В первой строке line[0] символ порядка байтов.
                line = line[1:]             # <- убираем первый символ из строки для корректной работы

            if is_date_first(line):
                if mode == '--module':
                    split_element = line[25:line.find(']', 25)]
                else:
                    split_element = line[0:10]

                log_file_name = f'trace_{split_element}.log'
                try:
                    if log_file_name in self.files:
                        self.current_file = self.files[log_file_name]
                        self.current_file.write(line)
                    else:
                        self.current_file = open(log_file_name, 'w')
                        self.files[log_file_name] = self.current_file
                        self.current_file.write(line)
                except FileNotFoundError:
                    self.write_to_basket(line)
                except PermissionError:
                    self.write_to_basket(line)
                except KeyError:
                    self.write_to_basket(line)
            else:
                if self.readed_data_size == 0:   # В случае если первая строка не содержит дату или модуль
                    self.write_to_basket(line)   # <- Записываем строки в _Unknown_.log пока не найдем их
                self.current_file.write(line)

            self.readed_data_size += len(line.encode('utf-8'))
            if self.readed_data_size > (PROGRESSBAR_STEP *
                                        self.progressbar_counter):
                self.progressbar_counter += 1
                update_progressbar(self.progressbar_counter)

    def write_to_basket(self, line: str):
        if '_Unknown_.log' in self.files.keys():
            self.current_file = self.files['_Unknown_.log']
        else:
            self.current_file = self.open_file('_Unknown_.log', 'w')
            self.files['_Unknown_.log'] = self.current_file
        self.current_file.write(line)

    def open_file(self, file_name, mode='r'):
        try:
            file = open(file_name, mode)
            return file
        except FileNotFoundError:
            print(f"Не удалось открыть файл: {file_name} файл не существует")
        except PermissionError:
            print(f"Не удалось открыть файл: {file_name} недостаточно прав")

    def __del__(self):
        for temp_file in self.files.values():
            temp_file.close()


def is_date_first(line: str) -> bool:
    return line[0].isdigit() \
           and line[1].isdigit() \
           and line[2] == '.' \
           and line[3].isdigit() \
           and line[4].isdigit() \
           and line[5] == '.' \
           and line[6].isdigit() \
           and line[7].isdigit() \
           and line[8].isdigit() \
           and line[9].isdigit()


def parse_args() -> tuple:
    try:
        mode = argv[1] if len(argv) > 1 else exit('bad args')
    except:
        raise Exception("Недостаточно аргументов")
    input_file = argv[2] if len(argv) > 2 else 'trace.log'
    return input_file, mode


def update_progressbar(progressbar_counter: int):
    print('\r', end='')
    print('[', end='')
    for i in range(10):
        if i < progressbar_counter:
            print('#', end='')
        else:
            print(' ', end='')
    print('] {}%'.format(int(progressbar_counter * 10)), end='')


def process():
    input_file_name, mode = parse_args()
    splitter = Spliter(input_file_name)
    splitter.split_files(mode)


start_time = time()

if __name__ == "__main__":
    try:
        process()
    except FileNotFoundError:
        pass
    except PermissionError:
        pass

print(f'\nОбщее время работы программы: {time() - start_time} сек.')
