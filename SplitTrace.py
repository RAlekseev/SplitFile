from time import time
from sys import argv, getsizeof
import os

class Spliter:
	files = {}

	def __init__(self, input_file):
		self.input_file_name = input_file
		self.current_recording_file = open('_Unknown_.log', 'w')
		self.files['_Unknown_.log'] = self.current_recording_file
		try:

			self.input_file = open(self.input_file_name, encoding = 'utf-8')
			self.files[self.input_file_name] = self.input_file
		except:
			exit('Не удалось открыть файл: ' + self.input_file_name)

	def split_files(self, mode: str):
		for line in self.input_file:
			if is_date_first(line):
				split_element = line.split()[2][1:-1] if mode == '--module' else line[0:10]
				log_file_name = 'trace_' + split_element + '.log'
				if log_file_name in self.files:
					self.current_recording_file = self.files[log_file_name]
					self.current_recording_file.write(line)
				else:
					self.current_recording_file = open( log_file_name, 'w')
					self.files[log_file_name] = self.current_recording_file
					self.current_recording_file.write(line)
			else:
				self.current_recording_file.write(line)


	def __del__(self):
		for temp_file in self.files.values():
			temp_file.close


def is_date_first(line : str) -> bool:
	return line[0].isdigit() \
	and line[1].isdigit()    \
	and line[2] == '.'       \
	and line[3].isdigit()    \
	and line[4].isdigit()    \
	and line[5] == '.'       \
	and line[6].isdigit()    \
	and line[7].isdigit()    \
	and line[8].isdigit()    \
	and line[9].isdigit()


start_time = time()

if __name__ == "__main__":
	mode = argv[1] if len(argv) > 1 else exit('bad args')
	input_file = argv[2] if len(argv) > 2 else 'trace.log'
	Spliter(input_file).split_files(mode)

print('\nОбщее время работы программы: ' + str(time() - start_time) + ' сек.')
