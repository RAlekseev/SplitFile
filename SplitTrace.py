from time import time
from sys import argv


def make_breaking_up(line,mode : str, current_recording_file):

	if is_date_first(line):
		breaking_up_element = line.split()[2][1:-1] if mode == '--module' else line[0:10] 
		if breaking_up_element in files.keys():
			current_recording_file = files[breaking_up_element]
			current_recording_file.write(line)
		else:
			current_recording_file = open( 'trace_' + breaking_up_element + '.log', 'w')
			files[breaking_up_element] = current_recording_file
			current_recording_file.write(line)
	else:
		current_recording_file.write(line)
	return current_recording_file


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
	try:
		f = open(input_file, encoding = 'utf-8')
	except:
		exit('Не удалось открыть файл: ' + input_file)
	
	current_recording_file = open('_Unknown_.log', 'w')
	files = {'Unknown': current_recording_file}

	for line in f:
		current_recording_file =  make_breaking_up(line, mode, current_recording_file)

	for file in files.values():
		file.close()
	f.close()
	
print(time() - start_time)
